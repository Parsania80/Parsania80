"""A restrained research feature with a meaningful TreeKEM topology illustration."""

from generate_assets import ASSETS, THEMES, editorial_svg, text


def tree(theme, cx, y, arity):
    parts = []
    points = [(cx, y)]
    if arity == 2:
        for parent in [cx - 40, cx + 40]:
            parts.append(f'<path d="M {cx} {y} L {parent} {y + 43}"/>')
            points.append((parent, y + 43))
            for leaf in [parent - 20, parent + 20]:
                parts.append(f'<path d="M {parent} {y + 43} L {leaf} {y + 86}"/>')
                points.append((leaf, y + 86))
    else:
        for leaf in [cx - 72, cx - 24, cx + 24, cx + 72]:
            parts.append(f'<path d="M {cx} {y} L {leaf} {y + 86}"/>')
            points.append((leaf, y + 86))
    lines = f'<g fill="none" stroke="{theme["muted"]}" stroke-width="1.7" opacity="0.65">' + ''.join(parts) + '</g>'
    nodes = ''.join(f'<circle cx="{x}" cy="{yy}" r="5.5" fill="{theme["text"]}"/>' for x, yy in points)
    return lines + nodes


def feature(theme, mobile=False):
    width, height = (680, 700) if mobile else (1200, 320)
    parts = [text(32, 42, 'RESEARCH / OPEN SOURCE', theme['muted'], 23 if mobile else 16, 500)]
    parts += [text(32, 105, 'Hybrid group key exchange', theme['text'], 44, 650), text(32, 157, 'with adaptive TreeKEM', theme['text'], 44, 650)]
    if mobile:
        parts += [text(32, 224, 'Rust research into MLS group messaging,', theme['muted'], 28), text(32, 263, 'hybrid key delivery and adaptive trees.', theme['muted'], 28)]
        parts += [text(32, 325, 'Master’s thesis · Cybersecurity', theme['text'], 26, 500), text(32, 425, 'TreeKEM arity transition', theme['muted'], 24)]
        y, left, right = 470, 180, 500
        parts += [text(32, 669, 'University of Isfahan · Source on GitHub', theme['muted'], 23)]
    else:
        parts += [text(32, 206, 'A Rust research prototype for MLS group messaging,', theme['muted'], 22), text(32, 238, 'hybrid key delivery, and adaptive tree transitions.', theme['muted'], 22)]
        parts += [text(32, 284, 'Master’s thesis · Cybersecurity · University of Isfahan', theme['muted'], 18), text(795, 58, 'TreeKEM arity transition', theme['muted'], 20)]
        y, left, right = 112, 866, 1090
    parts += [tree(theme, left, y, 2), tree(theme, right, y, 4), text((left + right) / 2, y + 49, '→', theme['muted'], 29, 400, 'text-anchor="middle"')]
    parts += [text(left, y + 131, 'Binary tree', theme['text'], 24 if mobile else 18, 500, 'text-anchor="middle"'), text(right, y + 131, 'Four-way tree', theme['text'], 24 if mobile else 18, 500, 'text-anchor="middle"')]
    return editorial_svg(width, height, ''.join(parts), 'Master-Hybrid-MLS — open-source master’s research on hybrid group key exchange, adaptive TreeKEM, and Rust implementation', theme)


def main():
    for mode, theme in THEMES.items():
        (ASSETS / f'research-{mode}.svg').write_text(feature(theme))
        (ASSETS / f'research-mobile-{mode}.svg').write_text(feature(theme, True))


if __name__ == '__main__':
    main()
