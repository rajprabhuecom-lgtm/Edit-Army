"""Render overlay frames: python3 render.py <worker> <nworkers> [frame list json]"""
import json, sys, os, asyncio
from playwright.async_api import async_playwright
FPS = 30
async def main(w, n, only):
    tl = json.load(open('/home/claude/w/gfx/timeline.json'))
    nfr = int(round(tl['total'] * FPS)); os.makedirs('/home/claude/w/ov', exist_ok=True)
    idx = only if only is not None else list(range(w, nfr, n))
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
        await pg.goto('file:///home/claude/w/gfx/engine.html'); await pg.evaluate('tl=>init(tl)', tl)
        await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
        for k, i in enumerate(idx):
            vis = await pg.evaluate(f'setT({i / FPS})')
            if vis: await pg.screenshot(path=f'/home/claude/w/ov/{i:05d}.png', omit_background=True)
            if k % 300 == 0: print(w, k, len(idx), flush=True)
        await b.close()
if __name__ == '__main__':
    only = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else None
    asyncio.run(main(int(sys.argv[1]), int(sys.argv[2]), only))
