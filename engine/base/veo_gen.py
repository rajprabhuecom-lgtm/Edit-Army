#!/usr/bin/env python3
"""Generate B-roll clips from a flow_prompts.json with Veo (the model behind Google Flow).

  GEMINI_API_KEY=... python3 engine/base/veo_gen.py videos/<id>/broll-ad/flow_prompts.json [--only D02,D03] [--takes 2] [--model veo-3.1-fast-generate-preview]
  python3 engine/base/veo_gen.py <json> --md      # write flow_prompts.md (paste-ready for Flow) and exit

Clips land next to the JSON in broll/<ID>_take<N>.mp4. Fallback shots (marked FALLBACK) are skipped unless --fallbacks.
"""
import argparse, json, os, re, sys, time, urllib.request

API = "https://generativelanguage.googleapis.com/v1beta"

def full_prompt(spec, shot):
    """Inline the character: 'NAME (see character, in X)' -> '<base>, in X,'; 'NAME (see character)' -> '<base>, <outfit>,'."""
    c, p = spec["character"], shot["prompt"]
    n = c["name"]
    p = re.sub(rf"{n}'s hands \(see character: ([^)]*)\)", r"her hands (\1)", p)
    p = re.sub(rf"{n} \(see character, ([^)]*)\)", lambda m: f"{c['inline']}, {m.group(1)},", p)
    p = p.replace(f"{n} (see character)", f"{c['inline']}, {c['outfit']},")
    p = p.replace(f"{n}'s", "her").replace(n, "the woman")
    p = re.sub(r",(\s*)(who|,)", r"\1\2", p).replace(",,", ",")
    p = re.sub(r"([.:]\s+)a South Indian", r"\1A South Indian", p)
    return p

def req(method, url, key, body=None):
    r = urllib.request.Request(url, method=method, headers={"x-goog-api-key": key, "Content-Type": "application/json"},
                               data=json.dumps(body).encode() if body else None)
    with urllib.request.urlopen(r, timeout=120) as f:
        return json.load(f)

def generate(key, model, prompt, negative, seconds, out):
    op = req("POST", f"{API}/models/{model}:predictLongRunning", key, {
        "instances": [{"prompt": prompt}],
        "parameters": {"aspectRatio": "9:16", "negativePrompt": negative, "durationSeconds": seconds, "resolution": "720p", "personGeneration": "allow_all"}})
    while not op.get("done"):
        time.sleep(10)
        op = req("GET", f"{API}/{op['name']}", key)
    if "error" in op:
        raise RuntimeError(op["error"])
    uri = op["response"]["generateVideoResponse"]["generatedSamples"][0]["video"]["uri"]
    r = urllib.request.Request(uri, headers={"x-goog-api-key": key})
    with urllib.request.urlopen(r, timeout=300) as f, open(out, "wb") as o:
        o.write(f.read())

def write_md(spec, path):
    L = [f"# {spec['video']}: Google Flow prompts (optimised)", "",
         f"**Upload to:** {spec['upload_to']}  ",
         f"**Flow settings:** {spec['settings']['aspect']}, {spec['settings']['seconds']} s, {spec['settings']['takes']} takes per shot, {spec['settings']['model']}.  ",
         "**Continuity:** every shot reuses the same character, so the problem montage reads as one person's story. In Flow, after the first good take, use its frame as an *Ingredient* / reference image for the other shots.", "",
         f"**Character (already pasted into each prompt):** {spec['character']['inline']}, {spec['character']['outfit']}. {spec['character']['note']}", "",
         "**Negative prompt (paste in the negative field, or at the end of the prompt):**", "```", spec["negative"], "```", ""]
    for s in spec["shots"]:
        L += [f"## {s['id']}: \"{s['line']}\"", f"*{s['use']}* · save as `{s['file']}`", "```", full_prompt(spec, s), "```", ""]
    L += ["## Not for Flow"] + [f"- {x}" for x in spec["not_flow"]] + ["",
          "## Check each take before keeping it",
          "- No text, numbers or logos appear anywhere (scale displays, phones and papers stay blurred)",
          "- Hands and faces aren't warped, and nobody looks into the lens",
          "- It looks Tamil Nadu (clothes, house and street), not generic stock",
          "- The action lands inside the first 4 s (the edit uses 3-5 s)",
          "- Respectful: struggle, not mockery",
          "", "Disclose AI in Meta (the 'AI info' toggle). AI is never used for coaches, members, results or testimonials."]
    open(path, "w").write("\n".join(L) + "\n")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json"); ap.add_argument("--only"); ap.add_argument("--takes", type=int, default=2)
    ap.add_argument("--model", default="veo-3.1-fast-generate-preview"); ap.add_argument("--fallbacks", action="store_true")
    ap.add_argument("--md", action="store_true")
    a = ap.parse_args()
    spec = json.load(open(a.json))
    base = os.path.dirname(os.path.abspath(a.json))
    if a.md:
        write_md(spec, os.path.join(base, "flow_prompts.md")); print("wrote flow_prompts.md"); return
    key = os.environ.get("GEMINI_API_KEY") or sys.exit("Set GEMINI_API_KEY")
    os.makedirs(os.path.join(base, "broll"), exist_ok=True)
    only = set(a.only.split(",")) if a.only else None
    for s in spec["shots"]:
        if only and s["id"] not in only: continue
        if "FALLBACK" in s["file"] and not a.fallbacks and not only: continue
        for t in range(1, a.takes + 1):
            out = os.path.join(base, "broll", s["file"].replace(".mp4", f"_take{t}.mp4"))
            if os.path.exists(out): print("skip", out); continue
            print("generating", s["id"], "take", t, flush=True)
            generate(key, a.model, full_prompt(spec, s), spec["negative"], spec["settings"]["seconds"], out)
            print("  ->", out, flush=True)

if __name__ == "__main__":
    main()
