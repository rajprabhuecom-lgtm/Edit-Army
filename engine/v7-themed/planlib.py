"""v7 plan builder. A video's plan.py describes its edit in SOURCE time and calls build(cfg).
Source time = time in W/src.mkv (one joined clip, or the voice-over for a faceless ad).

cfg keys
  KEEP   [(s, e), ...]           source ranges kept, in order (jump cuts). The last END_TAIL ranges sit under the end card.
  END_TAIL  int                  how many trailing KEEP ranges are end-card time (default 1)
  BROLL  [(id, s0, s1, scene, layout, extra, keyword)]   scene 'vid' = clip in W/broll (extra: file, ss, cy, des, chip)
  GFX    [(type, s0, s1, extra)] on-face / on-video graphics
  CAP    [(s0, s1, lead, keyword)]
  CAPSTYLE 'A' (lead above keyword) or 'B' (keyword above subline)
  PUNCH  [(s0, s1, zoom)]   PUSH [(s0, s1, z0, z1)]
  MUSIC  [(s0, mood)]       SFX [(t, name)]
  BRAND  dict for timeline.brand (badge, name, title, star, motif, poster, end)
Cue lists in extra (`cues`) are SOURCE times and become item-relative output times.
"""
import json, bisect, csv, os

def build(cfg, here):
    W = os.environ.get('W', '/home/user/w').rstrip('/') + '/'
    keep = [list(k) for k in cfg['KEEP']]
    ostarts = []; acc = 0
    for a, b in keep: ostarts.append(acc); acc += b - a
    TOTAL = acc; END_O = ostarts[-cfg.get('END_TAIL', 1)]

    def s2o(t):
        for (a, b), o in zip(keep, ostarts):
            if a <= t <= b: return o + (t - a)
        best = min(range(len(keep)), key=lambda i: min(abs(t - keep[i][0]), abs(t - keep[i][1])))
        a, b = keep[best]; return ostarts[best] + (0 if abs(t - a) < abs(t - b) else b - a)

    def o2s(t):
        i = max(0, bisect.bisect_right(ostarts, t) - 1); return keep[i][0] + (t - ostarts[i])

    items, captions, sfx = [], [], []
    for bid, s0, s1, sc, lay, ex, _ in cfg['BROLL']:
        o0, o1 = s2o(s0), s2o(s1); d = dict(type=sc, t0=o0, t1=o1, layout=lay, id=bid); ex = dict(ex)
        if 'cues' in ex:
            d['cues'] = [round(s2o(c) - o0, 3) for c in ex.pop('cues')]
            kind = {'stamps': 'thud', 'pinmap': 'pop', 'stuck': 'pop', 'choice': 'swipe'}.get(sc, 'tick')
            sfx += [(o0 + c, kind) for c in d['cues']]
        if 'scue' in ex: d['scue'] = round(s2o(ex.pop('scue')) - o0, 3); sfx.append((o0 + d['scue'], 'thud'))
        if sc == 'offer': sfx.append((o0 + 0.45, 'cash'))
        d.update(ex); items.append(d); sfx.append((o0 - 0.12, 'whoosh'))
    for ty, s0, s1, ex in cfg['GFX']:
        o0 = s2o(s0); d = dict(type=ty, t0=o0, t1=s2o(s1)); ex = dict(ex)
        if 'cues' in ex:
            d['cues'] = [round(s2o(c) - o0, 3) for c in ex.pop('cues')]; sfx += [(o0 + c, 'pop') for c in d['cues']]
        d.update(ex); items.append(d)
        if ty in ('badge', 'tslam', 'slam'): sfx.append((o0, 'pop'))
        if ty == 'cta': sfx.append((o0 + 0.35, 'tick'))
    items.append(dict(type='endcard', t0=END_O, t1=TOTAL)); sfx.append((END_O, 'hit'))
    items.append(dict(type='brand', t0=0, t1=END_O))
    for s0, s1, lead, kw in cfg['CAP']:
        captions.append(dict(t0=s2o(s0), t1=s2o(s1), lead=lead, kw=kw))
    for a, b in zip(captions, captions[1:]):
        if b['t0'] - a['t1'] < 0.45: a['t1'] = b['t0']
    for c in captions:
        mid = (c['t0'] + c['t1']) / 2
        c['pos'] = 'split' if any(it.get('layout') == 'split' and it['t0'] <= mid < it['t1'] for it in items) else 'face'
    tl = dict(items=items, captions=captions, total=TOTAL, capStyle=cfg.get('CAPSTYLE', 'A'), brand=cfg.get('BRAND', {}))
    json.dump(tl, open(W + 'gfx/timeline.json', 'w'), ensure_ascii=False)

    # FX: whip-zoom transitions into every B-roll / scene segment, camera shake on slams and stamps
    seg_starts = sorted({round(it['t0'], 3) for it in items if it.get('layout')} | {round(it['t1'], 3) for it in items if it.get('layout')})
    hits = [it['t0'] for it in items if it['type'] in ('slam', 'stamp', 'tslam')]
    hits += [it['t0'] + c for it in items if it['type'] in ('stamps',) for c in it.get('cues', [])]
    hits += [it['t0'] + it['scue'] for it in items if it['type'] == 'stuck' and 'scue' in it]
    fps = 30; frames = []
    for i in range(int(round(TOTAL * fps))):
        to = i / fps; ts = o2s(to); k = max(0, bisect.bisect_right(ostarts, to) - 1)
        z = 1.0 if k % 2 == 0 else 1.07
        for a, b, zz in cfg.get('PUNCH', []):
            if a <= ts <= b: z = zz
        for a, b, z0, z1 in cfg.get('PUSH', []):
            if a <= ts <= b: z = z0 + (z1 - z0) * (ts - a) / (b - a)
        L = None; V = None
        for it in items:
            if it.get('layout') and it['t0'] <= to < it['t1']:
                L = it['layout']
                if it['type'] == 'vid':
                    V = [it['file'], round(it.get('ss', 0) + to - it['t0'], 4), round((to - it['t0']) / (it['t1'] - it['t0']), 4), it.get('cy', 960), bool(it.get('des'))]
        tr = 1.0
        for st0 in seg_starts:
            if 0 <= to - st0 < 0.24: tr = min(tr, (to - st0) / 0.24)
        shk = max([max(0.0, 1 - (to - h) / 0.3) for h in hits if 0 <= to - h < 0.3] or [0.0])
        frames.append(dict(ts=round(ts, 4), z=round(z, 4), L=L, V=V, tr=round(tr, 3), shk=round(shk, 3)))
    json.dump(frames, open(W + 'frames.json', 'w'))

    mus = [(s2o(s), m) for s, m in cfg['MUSIC']]
    mus = [(a, (mus[i + 1][0] if i + 1 < len(mus) else TOTAL), m) for i, (a, m) in enumerate(mus)]
    sfxo = sorted([(round(t, 3), n) for t, n in sfx] + [(round(s2o(t), 3), n) for t, n in cfg.get('SFX', [])])
    json.dump(dict(keep=keep, music=mus, sfx=sfxo, total=TOTAL, end=END_O), open(W + 'audio/cues.json', 'w'))

    with open(os.path.join(here, 'broll_log.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['ID', 'Source (s)', 'Final time (s)', 'Line (meaning)', 'Visual', 'Source type', 'Layout', 'On-screen (s, final)', 'Status', 'Licence / note'])
        for bid, s0, s1, sc, lay, ex, kw in cfg['BROLL']:
            o0, o1 = s2o(s0), s2o(s1)
            if sc == 'vid':
                src, typ = ex['file'], ('client photo/footage' if not ex.get('ai') else 'AI (Google Flow)')
                lic = ex.get('note', 'client-supplied, real')
            else:
                src, typ, lic = f'animated "{sc}" scene (engine v7)', 'P5 motion graphics', ex.get('note', 'original - no licence needed')
            w.writerow([bid, f'{s0:.2f}-{s1:.2f}', f'{o0/1.2:.1f}-{o1/1.2:.1f}', kw, src, typ, lay, f'{(o1-o0)/1.2:.1f}', ex.get('status', 'rendered'), lic])
    cov = sum(it['t1'] - it['t0'] for it in items if it.get('layout'))
    print(f'total {TOTAL:.2f}s -> {TOTAL/1.2:.2f}s | end card at {END_O/1.2:.2f}s | B-roll {cov/TOTAL*100:.0f}% | captions {len(captions)} | sfx {len(sfxo)}')
