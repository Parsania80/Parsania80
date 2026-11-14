"""Original profile sections, linked stack chips, and data-driven activity SVGs."""

import json
import math
import re
from datetime import date, timedelta
from pathlib import Path

from generate_assets import ASSETS, THEMES, mono, svg, text, editorial_svg


STACK = [
    ('BACKEND & SYSTEMS', 'teal', [
        ('cplusplus', 'C++', 'C++', 'https://isocpp.org/'),
        ('qt', 'Qt', 'Qt', 'https://www.qt.io/'),
        ('drogon', 'Drogon', 'Dg', 'https://github.com/drogonframework/drogon'),
        ('go', 'Go', 'Go', 'https://go.dev/'),
        ('rust', 'Rust', 'Rs', 'https://www.rust-lang.org/'),
    ]),
    ('DATA & REAL-TIME', 'blue', [
        ('postgresql', 'PostgreSQL', 'Pg', 'https://www.postgresql.org/'),
        ('sqlite', 'SQLite', 'Sq', 'https://www.sqlite.org/'),
        ('drift', 'Drift', 'Dr', 'https://drift.simonbinder.eu/'),
        ('websocket', 'WebSockets', 'Ws', 'https://www.rfc-editor.org/rfc/rfc6455'),
        ('pgcron', 'pg_cron', 'Cr', 'https://github.com/citusdata/pg_cron'),
    ]),
    ('MOBILE & ARCHITECTURE', 'purple', [
        ('flutter', 'Flutter', 'Fl', 'https://flutter.dev/'),
        ('dart', 'Dart', 'Dt', 'https://dart.dev/'),
        ('bloc', 'BLoC / Cubit', 'Bc', 'https://bloclibrary.dev/'),
        ('getit', 'GetIt', 'Di', 'https://pub.dev/packages/get_it'),
    ]),
    ('DELIVERY & INFRASTRUCTURE', 'teal', [
        ('linux', 'Linux', 'Lx', 'https://www.kernel.org/'),
        ('jenkins', 'Jenkins', 'Jk', 'https://www.jenkins.io/'),
        ('gitlab', 'GitLab Registry', 'Gl', 'https://docs.gitlab.com/user/packages/package_registry/'),
        ('docker', 'Docker', 'Dk', 'https://www.docker.com/'),
        ('debian', 'Debian packages', 'Db', 'https://www.debian.org/doc/manuals/maint-guide/'),
        ('git', 'Git', 'Gt', 'https://git-scm.com/'),
    ]),
    ('QUALITY & SECURITY', 'amber', [
        ('playwright', 'Playwright', 'Pw', 'https://playwright.dev/'),
        ('fluttertest', 'Flutter Test', 'Ft', 'https://docs.flutter.dev/testing'),
        ('pkcs11', 'PKCS #11', 'Pk', 'https://www.oasis-open.org/committees/pkcs11/'),
        ('rsa', 'RSA-2048', 'R', 'https://www.rfc-editor.org/rfc/rfc8017'),
    ]),
]


def principles(t, mobile=False):
    width, height = (680, 640) if mobile else (1200, 250)
    specs = [
        ('01 / ARCHITECTURE', 'Separate responsibilities.', ['Controllers, services, middleware.', 'Domain logic behind clear boundaries.'], 'teal'),
        ('02 / VERIFICATION', 'Make behavior measurable.', ['API, UI, and scenario-based load tests.', 'Reusable flows for repeatable checks.'], 'purple'),
        ('03 / DELIVERY', 'Make releases repeatable.', ['Migrations, packages, and automation.', 'Build, install, test, and iterate.'], 'blue'),
    ]
    parts = []
    for i, (label, title, lines, accent) in enumerate(specs):
        x, y, w, h = (16, 12 + i * 208, 648, 198) if mobile else (12 + i * 398, 12, 380, 226)
        parts += [text(x + 22, y + 39, label, t['muted'], 21 if mobile else 15, 500), text(x + 22, y + 88, title, t['text'], 32 if mobile else 24, 600)]
        for j, line in enumerate(lines):
            parts.append(text(x + 22, y + 132 + j * 33, line, t['muted'], 25 if mobile else 18))
    return editorial_svg(width, height, ''.join(parts), 'How I work: clear architecture, measurable behavior, repeatable delivery', t)


def stack_assets():
    chunks = []
    target = ASSETS / 'stack'
    target.mkdir(exist_ok=True)
    for category, accent, items in STACK:
        chunks.append(f'**{category}**\n\n<p>')
        for slug, label, mark, url in items:
            width = 74 + len(label) * 9
            for mode, t in THEMES.items():
                content = f'<rect x="10" y="10" width="29" height="29" rx="8" fill="{t[accent]}"/>'
                content += text(24.5, 30, mark, t['bg'], 13, 750, 'text-anchor="middle"')
                content += text(50, 31, label, t['text'], 17, 600)
                (target / f'{slug}-{mode}.svg').write_text(svg(width, 49, content, label, t))
            chunks.append(f'<a href="{url}"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/{slug}-light.svg"><img src="assets/stack/{slug}-dark.svg" alt="{label}" height="44"></picture></a>')
        chunks.append('</p>\n')
    readme = ASSETS.parent / 'README.md'
    content = readme.read_text()
    content = re.sub(r'<!-- STACK:START -->[\s\S]*?<!-- STACK:END -->', '<!-- STACK:START -->\n' + '\n'.join(chunks) + '\n<!-- STACK:END -->', content)
    readme.write_text(content)


def activity(t, data, mobile=False):
    width, height = (680, 1110) if mobile else (1200, 590)
    parts = [mono(30, 43, 'GITHUB / VISIBLE ACTIVITY', t['teal'], 21 if mobile else 18), text(30, 77, data['period_label'], t['muted'], 22 if mobile else 18)]
    stats = [(f"{data['total_contributions']:,}", 'Contributions', 'GitHub-visible in this period', 'teal'), (str(data['active_days']), 'Active days', 'Days with recorded contributions', 'purple'), (str(data['public_repos']), 'Public repositories', f"{data['followers']} followers · {data['stars']} stars", 'blue')]
    for i, (value, label, detail, accent) in enumerate(stats):
        x, y, w, h = (24, 104 + i * 155, 632, 142) if mobile else (24 + i * 390, 107, 372, 168)
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="13" fill="{t["panel"]}" stroke="{t["line"]}"/>')
        parts += [text(x + 22, y + 58, value, t[accent], 49, 750), text(x + 22, y + 96, label, t['text'], 25 if mobile else 22, 650), text(x + 22, y + 126 if mobile else y + 136, detail, t['muted'], 21 if mobile else 17)]
    x, y, w = (24, 588, 632) if mobile else (24, 300, 1152)
    parts += [text(x + 10, y + 13, 'Public repository languages', t['text'], 27 if mobile else 24, 700), text(x + 10, y + 46, 'Share of code bytes · non-fork repositories', t['muted'], 21 if mobile else 18)]
    colors = [t['blue'], t['amber'], t['purple'], t['teal'], '#f4819f', '#d2c3ff']
    languages = list(data['languages'].items())
    total = sum(amount for _, amount in languages)
    current = x + 10
    for i, (label, amount) in enumerate(languages):
        length = (w - 20) * amount / max(total, 1)
        parts.append(f'<rect x="{current:.2f}" y="{y + 69}" width="{length:.2f}" height="17" fill="{colors[i % len(colors)]}"/>')
        current += length
    for i, (label, amount) in enumerate(languages):
        xx = x + 10 if mobile else x + 10 + (i % 2) * 570
        yy = y + 128 + i * 51 if mobile else y + 130 + (i // 2) * 42
        parts += [f'<circle cx="{xx + 7}" cy="{yy - 7}" r="6" fill="{colors[i % len(colors)]}"/>', text(xx + 25, yy, label, t['text'], 25 if mobile else 20, 550), text(xx + (590 if mobile else 510), yy, f'{amount / max(total, 1) * 100:.1f}%', t['muted'], 23 if mobile else 20, 500, 'text-anchor="end"')]
    parts += [mono(34, height - 27, 'Updated ' + data['updated'] + ' / GitHub public data', t['muted'], 19 if mobile else 16)]
    return svg(width, height, ''.join(parts), 'Actual GitHub contribution and public repository language statistics', t)


def contributions_3d(t, data):
    width, height = 1200, 640
    parts = [mono(32, 43, 'A YEAR IN COMMITS / CONTRIBUTION TERRAIN', t['teal'], 18), text(32, 77, data['period_label'] + ' · GitHub-visible contributions', t['muted'], 19)]
    days = {date.fromisoformat(d['date']): d for d in data['days']}
    first = min(days)
    start = first - timedelta(days=(first.weekday() + 1) % 7)
    origin_x, origin_y = 210, 170
    colors = [t['panel'], '#225b50', '#248b71', '#35bd91', '#5ee6c5'] if t is THEMES['dark'] else [t['panel'], '#bde7d9', '#7dccb5', '#38ab8a', '#087e69']
    # Genuine daily counts drive both height and color. The geometry is decorative.
    end = max(days)
    weeks = ((end - start).days // 7) + 1
    for week in range(weeks):
        for weekday in range(7):
            current = start + timedelta(days=week * 7 + weekday)
            day = days.get(current)
            if day is None:
                continue
            count, level = day['count'], day['level']
            x = origin_x + week * 18 - weekday * 18
            y = origin_y + week * 7 + weekday * 7
            rise = 0 if not count else 10 + 12 * math.log2(count + 1)
            color = colors[min(level, 4)]
            top = f'{x},{y - rise} {x + 17},{y + 6 - rise} {x},{y + 12 - rise} {x - 17},{y + 6 - rise}'
            title = f'{current.isoformat()}: {count} contributions'
            parts.append(f'<g><title>{title}</title>')
            if rise:
                parts.append(f'<polygon points="{x - 17},{y + 6 - rise} {x},{y + 12 - rise} {x},{y + 12} {x - 17},{y + 6}" fill="{color}" opacity="0.55"/>')
                parts.append(f'<polygon points="{x},{y + 12 - rise} {x + 17},{y + 6 - rise} {x + 17},{y + 6} {x},{y + 12}" fill="{color}" opacity="0.8"/>')
            parts.append(f'<polygon points="{top}" fill="{color}" stroke="{t["line"]}" stroke-width="0.7"/></g>')
    parts += [text(34, 598, f"{data['total_contributions']:,} contributions", t['teal'], 30, 700), text(460, 598, 'Each tile = one day. Height = contribution count.', t['muted'], 20)]
    return svg(width, height, ''.join(parts), 'Isometric contribution calendar built from real daily GitHub activity', t)


def main():
    stack_assets()
    from forg_panels import main as forg_panels
    forg_panels()
    from research_feature import main as research_feature
    research_feature()
    for mode, t in THEMES.items():
        for mobile in [False, True]:
            suffix = f'mobile-{mode}' if mobile else mode
            (ASSETS / f'principles-{suffix}.svg').write_text(principles(t, mobile))
    source = ASSETS / 'activity-data.json'
    if source.exists():
        data = json.loads(source.read_text())
        for mode, t in THEMES.items():
            (ASSETS / f'activity-{mode}.svg').write_text(activity(t, data))
            (ASSETS / f'activity-mobile-{mode}.svg').write_text(activity(t, data, True))
            (ASSETS / f'contributions-3d-{mode}.svg').write_text(contributions_3d(t, data))
    print('Generated FORG panels, principles, linked stack chips, and activity sections.')


if __name__ == '__main__':
    main()
