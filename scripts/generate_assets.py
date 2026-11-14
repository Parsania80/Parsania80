#!/usr/bin/env python3
"""Generate original, self-contained SVG artwork for the GitHub profile."""

from html import escape
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
THEMES = {
    "dark": {"bg": "#0b1120", "panel": "#101b2f", "line": "#27364d", "text": "#eff5ff", "muted": "#a5b5cc", "teal": "#5ee6c5", "purple": "#b8a1ff", "blue": "#7dbbff", "amber": "#ffc483"},
    "light": {"bg": "#f5f8ff", "panel": "#ffffff", "line": "#d5dfed", "text": "#14243c", "muted": "#51647d", "teal": "#087e69", "purple": "#6d49c5", "blue": "#2368b4", "amber": "#93520e"},
}


def svg(width, height, content, title, theme):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title, quote=True)}">
<title>{escape(title)}</title>
<defs><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M 32 0 L 0 0 0 32" fill="none" stroke="{theme['line']}" stroke-width="0.7" opacity="0.4"/></pattern></defs>
<rect x="0.75" y="0.75" width="{width - 1.5}" height="{height - 1.5}" rx="22" fill="{theme['bg']}" stroke="{theme['line']}" stroke-width="1.5"/>
<g font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif">{content}</g>
</svg>\n'''


def text(x, y, value, fill, size=22, weight=400, extra=""):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-weight="{weight}" {extra}>{escape(value)}</text>'


def mono(x, y, value, fill, size=16):
    return text(x, y, value, fill, size, 500, 'font-family="ui-monospace,SFMono-Regular,Consolas,monospace"')


def editorial_svg(width, height, content, title, theme):
    """One quiet surface; no colored edge, inset boxes, or decorative trim."""
    dark = theme is THEMES['dark']
    surface, border = ('#11161d', '#2b333d') if dark else ('#fafbfc', '#d6dde5')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title, quote=True)}"><title>{escape(title)}</title><rect x="0.75" y="0.75" width="{width - 1.5}" height="{height - 1.5}" rx="14" fill="{surface}" stroke="{border}" stroke-width="1.5"/><g font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif">{content}</g></svg>\n'''


def editorial_accent(theme, warm=False):
    """Two soft ink colors keep the work sections cohesive and readable."""
    if theme is THEMES['dark']:
        return '#d5b586' if warm else '#83cbb8'
    return '#866022' if warm else '#26745f'


def chip(x, y, label, t, color=None):
    width = 26 + len(label) * 9
    return f'<rect x="{x}" y="{y}" width="{width}" height="32" rx="9" fill="{t["panel"]}" stroke="{t["line"]}"/>' + text(x + 13, y + 22, label, color or t["muted"], 16, 500), width


def hero(t):
    parts = ['<rect x="745" y="2" width="453" height="428" rx="20" fill="url(#grid)"/>']
    parts += [mono(48, 49, 'PARSANIA80  /  ENGINEERING & PRODUCTS', t['teal'], 17)]
    parts += [text(48, 129, 'Mohammadreza', t['text'], 64, 750), text(48, 203, 'Parsania.', t['purple'], 76, 750)]
    parts += [text(50, 253, 'Backend developer. Product builder.', t['text'], 28, 550)]
    parts += [text(50, 292, 'C++ services, real-time systems, and the tools', t['muted'], 22), text(50, 323, 'that turn working code into shipped software.', t['muted'], 22)]
    x = 50
    for label in ['C++', 'PostgreSQL', 'Go', 'Rust', 'Flutter']:
        element, width = chip(x, 357, label, t)
        parts.append(element)
        x += width + 10
    parts += [mono(799, 67, 'BUILD / TEST / SHIP', t['muted'], 17)]
    parts += [f'<path d="M 836 134 H 795 V 296 H 836 M 795 215 H 836" fill="none" stroke="{t["teal"]}" stroke-width="2"/>']
    for y, label, subtitle, accent, number in [(97,'SERVICES','C++ / Qt / Drogon','teal','01'),(178,'DATA','PostgreSQL / real-time','purple','02'),(259,'DELIVERY','CI/CD / packages / tests','blue','03')]:
        parts.append(f'<rect x="836" y="{y}" width="315" height="68" rx="12" fill="{t["panel"]}" stroke="{t["line"]}"/>')
        parts += [mono(852, y + 28, number, t[accent], 17), text(890, y + 28, label, t[accent], 17, 700), text(890, y + 51, subtitle, t['muted'], 16)]
    parts += [f'<circle cx="803" cy="374" r="5" fill="{t["teal"]}"/>', mono(818, 380, 'BACKEND DEVELOPER @ EEPACO', t['muted'], 16)]
    return svg(1200, 432, ''.join(parts), 'Mohammadreza Parsania — Backend Developer & Product Builder', t)


def mobile_hero(t):
    parts = [mono(36, 48, 'PARSANIA80 / BACKEND & PRODUCTS', t['teal'], 21)]
    parts += [text(34, 136, 'Mohammadreza', t['text'], 62, 750), text(34, 212, 'Parsania.', t['purple'], 78, 750)]
    parts += [text(36, 275, 'Backend developer.', t['text'], 34, 600), text(36, 318, 'Product builder.', t['text'], 34, 600)]
    parts += [text(36, 378, 'Real-time systems. PostgreSQL.', t['muted'], 27), text(36, 416, 'From working code to shipped software.', t['muted'], 27)]
    parts += [f'<path d="M 36 452 H 644" stroke="{t["line"]}"/>', f'<circle cx="43" cy="495" r="6" fill="{t["teal"]}"/>', mono(62, 503, 'BACKEND DEVELOPER @ EEPACO', t['muted'], 23)]
    return svg(680, 540, ''.join(parts), 'Mohammadreza Parsania — Backend Developer & Product Builder', t)


PROJECTS = [
    {'file': 'forg', 'name': 'FORG', 'eyebrow': '01 / COMPANY WORK', 'state': 'PRIVATE', 'accent': 'teal', 'lines': ['Backend & device communication.', 'Real-time systems. Reliable delivery.'], 'stack': 'C++ / Qt / Drogon / PostgreSQL', 'footer': 'BACKEND DEVELOPER @ EEPACO', 'icon': 'server'},
    {'file': 'planner', 'name': 'Daily Planner', 'eyebrow': '02 / MY OWN PRODUCT', 'state': 'PRIVATE', 'accent': 'purple', 'lines': ['Offline-first planning. Clean architecture.', 'BLoC / Cubit state. SQLite persistence.'], 'stack': 'Flutter / Dart / Drift / BLoC', 'footer': 'MYKET & CAFE BAZAAR / OWNER', 'icon': 'calendar'},
    {'file': 'fluxget', 'name': 'FluxGet', 'eyebrow': '03 / OPEN SOURCE', 'state': 'PUBLIC', 'accent': 'blue', 'lines': ['A download manager built in Go.', 'Made for Linux & Windows.'], 'stack': 'Go / Desktop / Download engine', 'footer': 'EXPLORE SOURCE ON GITHUB', 'icon': 'download'},
    {'file': 'backup', 'name': 'parsBackUp', 'eyebrow': '04 / OPEN SOURCE', 'state': 'PUBLIC', 'accent': 'amber', 'lines': ['PostgreSQL backup & restore.', 'Built in Rust. Under development.'], 'stack': 'Rust / PostgreSQL 16 · 17 · 18', 'footer': 'EXPLORE SOURCE ON GITHUB', 'icon': 'database'},
]


def icon(kind, x, y, color):
    shapes = {
        'server': '<rect x="0" y="0" width="38" height="15" rx="4"/><rect x="0" y="23" width="38" height="15" rx="4"/><path d="M 8 7.5 H 12 M 8 30.5 H 12 M 23 7.5 H 30 M 23 30.5 H 30"/>',
        'calendar': '<rect x="0" y="4" width="38" height="34" rx="5"/><path d="M 0 15 H 38 M 10 0 V 9 M 28 0 V 9 M 10 26 L 16 31 L 28 21"/>',
        'download': '<path d="M 19 0 V 26 M 8 15 L 19 26 L 30 15 M 0 29 V 38 H 38 V 29"/>',
        'database': '<ellipse cx="19" cy="7" rx="19" ry="7"/><path d="M 0 7 V 31 C 0 41 38 41 38 31 V 7 M 0 19 C 0 29 38 29 38 19"/>',
    }
    return f'<g transform="translate({x} {y})" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{shapes[kind]}</g>'


def card(project, t):
    labels = {'forg': 'COMPANY WORK · PRIVATE SOURCE', 'planner': 'PERSONAL PRODUCT · PRIVATE SOURCE', 'fluxget': 'OPEN SOURCE · GO', 'backup': 'OPEN SOURCE · RUST'}
    accent = editorial_accent(t, project['state'] == 'PUBLIC')
    parts = [text(30, 37, labels[project['file']], accent, 14, 500),
             f'<circle cx="507" cy="85" r="31" fill="{accent}" fill-opacity="0.09"/>',
             icon(project['icon'], 488, 66, accent)]
    parts += [text(30, 106, project['name'], t['text'], 42, 650)]
    for i, line in enumerate(project['lines']):
        parts.append(text(30, 151 + i * 31, line, t['muted'], 21))
    footers = {'forg': 'Backend developer at EEPACO', 'planner': 'Available on Myket & Cafe Bazaar', 'fluxget': 'Explore the download manager', 'backup': 'Explore the backup platform'}
    parts += [text(30, 227, project['stack'], accent, 17), text(30, 277, footers[project['file']], t['text'], 16, 500), text(506, 279, '↗', accent, 24)]
    return editorial_svg(560, 306, ''.join(parts), project['name'] + ' — ' + ' '.join(project['lines']), t)


def mobile_card(project, t):
    tag = 'PRIVATE' if project['state'] == 'PRIVATE' else 'OPEN SOURCE'
    accent = editorial_accent(t, project['state'] == 'PUBLIC')
    parts = [text(30, 48, tag, accent, 25, 500),
             f'<circle cx="499" cy="43" r="31" fill="{accent}" fill-opacity="0.09"/>',
             icon(project['icon'], 480, 24, accent)]
    parts += [text(28, 128, project['name'], t['text'], 51, 650)]
    lines = {'forg': ['Backend & device', 'communication.'], 'planner': ['Flutter / BLoC.', 'Drift / SQLite.'], 'fluxget': ['Go downloads.', 'Linux & Windows.'], 'backup': ['Rust backups.', 'PostgreSQL 16–18.']}[project['file']]
    for i, line in enumerate(lines):
        parts.append(text(30, 200 + i * 52, line, t['muted'], 37))
    parts += [text(30, 337, 'View project', t['text'], 28, 500), text(493, 338, '↗', accent, 34)]
    return editorial_svg(560, 370, ''.join(parts), project['name'] + ' — ' + ' '.join(project['lines']), t)


def footer(t):
    parts = [mono(30, 42, 'PARSANIA80', t['teal'], 19), text(250, 42, 'Backend, products, and the tools that ship them.', t['muted'], 21)]
    return svg(1200, 68, ''.join(parts), 'Backend, products, and the tools that ship them.', t)


def button(label, width, mark, accent):
    t = THEMES['dark']
    parts = [text(15, 25, mark, accent, 18, 700), text(46, 25, label, t['text'], 15, 600)]
    return svg(width, 38, ''.join(parts), label, t)


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    for mode, theme in THEMES.items():
        (ASSETS / f'hero-{mode}.svg').write_text(hero(theme))
        (ASSETS / f'hero-mobile-{mode}.svg').write_text(mobile_hero(theme))
        (ASSETS / f'footer-{mode}.svg').write_text(footer(theme))
        for project in PROJECTS:
            (ASSETS / f'{project["file"]}-{mode}.svg').write_text(card(project, theme))
            (ASSETS / f'{project["file"]}-mobile-{mode}.svg').write_text(mobile_card(project, theme))
    for name, label, width, mark, accent in [('linkedin','LinkedIn',139,'in','#7dbbff'),('email','Email me',146,'@','#b8a1ff'),('phone','+98 939 600 3945',220,'☎','#5ee6c5'),('opensource','Open source',170,'↗','#5ee6c5')]:
        (ASSETS / f'{name}.svg').write_text(button(label, width, mark, accent))
    from profile_sections import main as sections
    sections()
    print(f'Generated {len(list(ASSETS.glob("*.svg")))} SVG assets in {ASSETS}')


if __name__ == '__main__':
    main()
