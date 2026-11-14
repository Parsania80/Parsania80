"""Visible, responsive FORG contribution panels with contextual outcomes."""

from html import escape
import re
from textwrap import wrap

from generate_assets import ASSETS, THEMES, mono, editorial_svg, editorial_accent, text


PANELS = [
    {
        'slug': 'backend', 'title': 'Backend & real-time features', 'accent': 'teal',
        'subtitle': 'C++ / Qt / Drogon / PostgreSQL',
        'rows': [
            ('Architecture', 'Controller, service and middleware layers in C++, Qt and Drogon.'),
            ('Backend features', 'Syslog, admin access, a backup service and API-based AI review.'),
            ('Database performance', 'Batched SQL queries and PostgreSQL notification listeners.'),
            ('Live dashboards', 'Real-time dashboard updates over WebSocket connections.'),
        ],
        'outcome': ('REAL-TIME FEATURES', 'WebSocket', ['Live dashboard updates'], ['C++ services built with', 'Qt and Drogon.']),
    },
    {
        'slug': 'server', 'title': 'Device server & connection handling', 'accent': 'blue',
        'subtitle': 'Mobile devices / WebSockets / Event-driven updates',
        'rows': [
            ('Device communication', 'WebSocket connections for mobile devices.'),
            ('Database efficiency', 'Batch-query optimization and PostgreSQL LISTEN/NOTIFY updates.'),
            ('Memory ownership', 'Smart pointers for object lifetimes and resource management.'),
        ],
        'outcome': ('CONNECTION LOAD TESTING', '100,000', ['Concurrent device', 'connections'], ['Designed for this workload;', 'validated with our device', 'connection tester.']),
    },
    {
        'slug': 'delivery', 'title': 'CI/CD, migrations & packaging', 'accent': 'purple',
        'subtitle': 'Jenkins / GitLab Package Registry / Debian',
        'rows': [
            ('Database delivery', 'Versioned SQL migrations and nightly maintenance with pg_cron.'),
            ('Build & release', 'Custom Jenkins parameters, package publishing and GitLab releases.'),
            ('Infrastructure scripts', 'Automated updates for the GitLab Docker deployment.'),
            ('Debian packages', 'Dependency metadata and post-installation configuration.'),
        ],
        'outcome': ('FORG RELEASE PACKAGING', '.deb', ['Backend & frontend', 'Database & device server'], ['Packaging all four components', 'with dependency rules and', 'post-installation scripts.']),
    },
    {
        'slug': 'testing', 'title': 'API, UI & stress testing', 'accent': 'amber',
        'subtitle': 'API checks / Playwright / Reusable test flows',
        'rows': [
            ('API & UI coverage', 'API tests and Playwright UI tests for product behavior.'),
            ('Reusable access tests', 'Flow-based administrator-access test implementation.'),
            ('Load scenarios', 'Stress-test scenarios and simulated device connection testing.'),
        ],
        'outcome': ('ADMIN-ACCESS TEST WORK', '14 days', ['To implement admin-access', 'tests'], ['Reduced from 3 months', 'by using reusable test flows.']),
    },
    {
        'slug': 'deployment', 'title': 'Automated deployment', 'accent': 'teal',
        'subtitle': 'Build automation / Local servers / Faster test cycles',
        'rows': [
            ('Build-to-install automation', 'A complete build and deployment system for local test servers.'),
            ('Repeatable environments', 'Connected build, package, installation and deployment steps.'),
            ('Testing workflow', 'Faster iteration through automated local-server deployment.'),
        ],
        'outcome': ('LOCAL TEST ENVIRONMENTS', 'Build → deploy', ['Repeatable server setup'], ['Build, package and install', 'through an automated workflow.']),
    },
    {
        'slug': 'licensing', 'title': 'Licensing & cryptography', 'accent': 'purple',
        'subtitle': 'In-memory licensing / PKCS #11 / RSA-2048',
        'rows': [
            ('License handling', 'In-memory processing of license information.'),
            ('Cryptographic integration', 'PKCS #11 integration for cryptographic operations.'),
            ('License signatures', 'RSA-2048 signing of license information.'),
        ],
        'outcome': ('LICENSE INFORMATION SIGNING', 'RSA-2048', ['PKCS #11 integration'], ['In-memory license handling', 'and cryptographic signing.']),
    },
]


def description(panel):
    result = panel['title'] + '. ' + ' '.join(f'{label}: {body}' for label, body in panel['rows'])
    _, value, units, details = panel['outcome']
    return result + ' ' + value + ': ' + ' '.join(units + details)


def render(panel, number, theme, mobile=False):
    width = 680 if mobile else 1200
    accent = editorial_accent(theme, panel['slug'] in ('delivery', 'testing'))
    parts = [text(30, 53, f'{number:02}', accent, 23, 500)]
    title_lines = wrap(panel['title'], 29) if mobile else [panel['title']]
    for i, line in enumerate(title_lines):
        parts.append(text(88, 53 + i * 39, line, theme['text'], 31, 650))
    subtitle_y = 84 + (len(title_lines) - 1) * 39
    for i, line in enumerate(wrap(panel['subtitle'], 40) if mobile else [panel['subtitle']]):
        parts.append(text(88, subtitle_y + i * 26, line, theme['muted'], 21 if mobile else 19, 400))
    header_end = subtitle_y + (len(wrap(panel['subtitle'], 40)) - 1) * 26 + 22 if mobile else 106
    y = header_end + 38
    for label, body in panel['rows']:
        parts.append(text(32, y, label, theme['text'], 27 if mobile else 22, 600))
        lines = wrap(body, 45 if mobile else 70, break_long_words=False, break_on_hyphens=False)
        for line in lines:
            y += 33 if mobile else 28
            parts.append(text(32, y, line, theme['muted'], 26 if mobile else 21))
        y += 29 if mobile else 34
    label, value, units, details = panel['outcome']
    outcome_height = 135 + len(units) * (32 if mobile else 28) + 11 + len(details) * (29 if mobile else 26) + 15
    if mobile:
        bx, by, bw, bh = 28, y + 4, 624, max(250, outcome_height)
        height = by + bh + 25
    else:
        height = max(420, y + 14, 150 + outcome_height)
        bx, by, bw, bh = 850, 123, 322, height - 150
    parts.append(text(bx + 4, by + 34, label.capitalize().replace('Forg', 'FORG'), accent, 23 if mobile else 17, 400))
    value_size = 49 if mobile else (34 if len(value) > 10 else 46)
    parts.append(text(bx + 4, by + 94, value, accent, value_size, 650))
    yy = by + 135
    for line in units:
        parts.append(text(bx + 4, yy, line, theme['text'], 26 if mobile else 21, 500))
        yy += 32 if mobile else 28
    yy += 11
    for line in details:
        parts.append(text(bx + 4, yy, line, theme['muted'], 24 if mobile else 19))
        yy += 29 if mobile else 26
    return editorial_svg(width, height, ''.join(parts), description(panel), theme)


def main():
    target = ASSETS / 'forg'
    target.mkdir(exist_ok=True)
    chunks = []
    for i, panel in enumerate(PANELS, 1):
        for mode, theme in THEMES.items():
            (target / f'{panel["slug"]}-{mode}.svg').write_text(render(panel, i, theme))
            (target / f'{panel["slug"]}-mobile-{mode}.svg').write_text(render(panel, i, theme, True))
        alt = escape(description(panel), quote=True)
        base = f'assets/forg/{panel["slug"]}'
        chunks.append(f'<p>\n<picture><source media="(max-width: 640px) and (prefers-color-scheme: light)" srcset="{base}-mobile-light.svg"><source media="(max-width: 640px)" srcset="{base}-mobile-dark.svg"><source media="(prefers-color-scheme: light)" srcset="{base}-light.svg"><img src="{base}-dark.svg" alt="{alt}" width="100%"></picture>\n</p>')
    readme = ASSETS.parent / 'README.md'
    content = readme.read_text()
    content = re.sub(r'<!-- FORG:START -->[\s\S]*?<!-- FORG:END -->', '<!-- FORG:START -->\n' + '\n\n'.join(chunks) + '\n<!-- FORG:END -->', content)
    readme.write_text(content)


if __name__ == '__main__':
    main()
