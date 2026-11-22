"""Small helpers so each 202603 plan.py stays short. All times are SOURCE seconds."""
def badge(t0, t1, html, bg='var(--rd)', fg='#fff', size=58, y=230): return ('badge', t0, t1, dict(html=html, bg=bg, fg=fg, size=size, y=y))
def yb(t0, t1, html, size=58, y=230): return badge(t0, t1, html, 'var(--yl)', '#000', size, y)
def gb(t0, t1, html, size=58, y=230): return badge(t0, t1, html, 'var(--em)', '#04110c', size, y)
def db(t0, t1, html, size=58, y=230): return badge(t0, t1, html, 'var(--ob)', '#fff', size, y)
def slam(t0, t1, html, size=110, y=200): return ('text', t0, t1, dict(html=html, size=size, y=y))
def stat(t0, t1, val, label='', pre='', suf='', y=200, size=220, col='var(--yl)', dec=0): return ('stat', t0, t1, dict(val=val, label=label, pre=pre, suf=suf, y=y, size=size, col=col, dec=dec))
def cta(t0, t1, label, badge=None, y=1000, arrow=''): return ('cta', t0, t1, dict(label=label, badge=badge, y=y, arrow=arrow))
def boom(t0, t1=None, emo=None, y=1100): return ('confetti', t0, t1 or t0 + 1.6, dict(emo=emo or ['🔥', '💥', '⭐', '🚀'], y=y))
def flash(t): return ('flash', t, t + 0.12, {})
def end(END, HOLD, emo, l1, l2, btn='➕ FOLLOW FOR MORE', l3='PROFITSOUL', ts=110, ts2=80):
    return [flash(END), ('endcard2', END, END + HOLD, dict(emo=emo, l1=l1, l2=l2, btn=btn, l3=l3, ts=ts, ts2=ts2))]
