#!/usr/bin/env python3
"""Render the actual README into local GitHub-like previews for visual review."""

from pathlib import Path
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / '.preview'
OUTPUT.mkdir(exist_ok=True)
body = MarkdownIt('commonmark', {'html': True}).enable('table').render((ROOT / 'README.md').read_text())
body = body.replace('src="assets/', 'src="../assets/').replace('srcset="assets/', 'srcset="../assets/')
css = '''
* {box-sizing:border-box} body {margin:0;font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif;background:var(--bg);color:var(--text)}
.shell {max-width:1040px;margin:36px auto;padding:0 24px} .breadcrumb {font:13px ui-monospace,monospace;color:var(--muted);margin:0 0 15px}
article {padding:32px;border:1px solid var(--line);border-radius:12px;background:var(--bg)} img {max-width:100%;height:auto;vertical-align:middle}
img[height="36"] {height:36px;width:auto} a {color:var(--link);text-decoration:none} a:hover {text-decoration:underline}
img[height="44"] {height:44px;width:auto;margin:3px 0}
h2 {font-size:24px;line-height:1.4;border-bottom:1px solid var(--line);padding-bottom:10px;margin-top:36px} h3 {font-size:20px;margin-top:28px;margin-bottom:10px}
p {margin-top:0;margin-bottom:18px} details {border:1px solid var(--line);border-radius:9px;margin:10px 0;padding:14px 18px} summary {cursor:pointer} details[open] summary {margin-bottom:18px}
li {margin:7px 0} table {border-collapse:collapse;display:block;overflow:auto;width:100%;margin:18px 0 30px} td,th {border:1px solid var(--line);padding:9px 14px;text-align:left}
tr:nth-child(even) {background:var(--panel)} :target {scroll-margin-top:20px} picture {display:inline} hr {border:0;border-top:1px solid var(--line)}
@media(max-width:600px){.shell {margin:16px auto;padding:0 10px}article{padding:16px}body{font-size:15px}h2{font-size:22px}h3{font-size:19px}details{padding:12px}}
'''
themes = {
    'dark': '--bg:#0d1117;--text:#e6edf3;--muted:#8b949e;--line:#30363d;--panel:#161b22;--link:#79c0ff;color-scheme:dark;',
    'light': '--bg:#fff;--text:#1f2328;--muted:#59636e;--line:#d1d9e0;--panel:#f6f8fa;--link:#0969da;color-scheme:light;',
}
import re
for theme, variables in themes.items():
    themed_body = body
    if theme == 'light':
        # Force the light artwork even if the browser itself uses a dark theme.
        themed_body = themed_body.replace(' and (prefers-color-scheme: light)', '').replace('(prefers-color-scheme: light)', 'all').replace('-dark.svg', '-light.svg')
    else:
        themed_body = re.sub(r'<source[^>]*prefers-color-scheme: light[^>]*>', '', themed_body)
    themed_body = re.sub(r'<h([23])>(.*?)</h\1>', lambda m: f'<h{m[1]} id="{re.sub(r"[^a-z0-9 -]", "", m[2].lower()).replace(" ", "-")}">{m[2]}</h{m[1]}>', themed_body)
    html = f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Parsania80 · Profile preview ({theme})</title><style>:root{{{variables}}}{css}</style><main class="shell"><p class="breadcrumb">Parsania80 / README.md · local preview</p><article>{themed_body}</article></main></html>'
    (OUTPUT / f'{theme}.html').write_text(html)
    print(OUTPUT / f'{theme}.html')
