#!/usr/bin/env python3
"""Fetch public GitHub metadata and visible calendar counts, then render assets."""

import argparse
import json
import os
import re
import urllib.request
from collections import Counter
from datetime import datetime, date
from html import unescape
from html.parser import HTMLParser
from zoneinfo import ZoneInfo

from generate_assets import ASSETS

USER = 'Parsania80'


def fetch(url, api=False):
    headers = {'User-Agent': 'Parsania80-profile', 'Accept': 'application/vnd.github+json' if api else 'text/html'}
    token = os.environ.get('GITHUB_TOKEN')
    if api and token:
        headers['Authorization'] = 'Bearer ' + token
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=35) as response:
        raw = response.read().decode()
    return json.loads(raw) if api else raw


class CalendarParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cells = {}
        self.counts = {}
        self.current_tip = None
        self.tip_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'td' and 'data-date' in attrs:
            self.cells[attrs['id']] = {'date': attrs['data-date'], 'level': int(attrs['data-level'])}
        if tag == 'tool-tip':
            self.current_tip = attrs.get('for')
            self.tip_text = []

    def handle_data(self, data):
        if self.current_tip:
            self.tip_text.append(data)

    def handle_endtag(self, tag):
        if tag == 'tool-tip' and self.current_tip:
            text = unescape(''.join(self.tip_text)).strip()
            match = re.match(r'([\d,]+) contributions? on ', text)
            if match:
                self.counts[self.current_tip] = int(match[1].replace(',', ''))
            elif text.startswith('No contributions on '):
                self.counts[self.current_tip] = 0
            self.current_tip = None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--as-of', type=date.fromisoformat, default=datetime.now(ZoneInfo('Asia/Tehran')).date())
    args = parser.parse_args()
    end = args.as_of
    start = date(end.year, 1, 1)
    user = fetch(f'https://api.github.com/users/{USER}', True)
    repos = []
    page = 1
    while True:
        batch = fetch(f'https://api.github.com/users/{USER}/repos?per_page=100&page={page}', True)
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    languages = Counter()
    for repo in repos:
        if not repo['fork']:
            languages.update(fetch(f'https://api.github.com/repos/{USER}/{repo["name"]}/languages', True))
    calendar = CalendarParser()
    calendar.feed(fetch(f'https://github.com/users/{USER}/contributions?from={start}&to={end}'))
    selected = {key: cell for key, cell in calendar.cells.items() if start.isoformat() <= cell['date'] <= end.isoformat()}
    expected = (end - start).days + 1
    if len(selected) != expected or any(key not in calendar.counts for key in selected):
        raise RuntimeError('GitHub calendar is incomplete or its markup changed; preserving the previous snapshot.')
    days = sorted([{**cell, 'count': calendar.counts[key]} for key, cell in selected.items()], key=lambda day: day['date'])
    display_languages = dict(languages.most_common(5))
    remaining_bytes = sum(languages.values()) - sum(display_languages.values())
    if remaining_bytes:
        display_languages['Other'] = remaining_bytes
    data = {
        'username': USER, 'updated': end.isoformat(), 'period_label': f'{start:%d %b %Y} — {end:%d %b %Y}',
        'total_contributions': sum(day['count'] for day in days), 'active_days': sum(day['count'] > 0 for day in days),
        'public_repos': user['public_repos'], 'followers': user['followers'], 'stars': sum(repo['stargazers_count'] for repo in repos),
        'languages': display_languages, 'days': days,
        'scope': 'GitHub-visible calendar; language bytes from public non-fork repositories only.',
        'sources': [f'https://github.com/{USER}', f'https://api.github.com/users/{USER}', f'https://api.github.com/users/{USER}/repos'],
    }
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / 'activity-data.json').write_text(json.dumps(data, indent=2) + '\n')
    from profile_sections import main as render
    render()
    print(f'Fetched {len(days)} days: {data["total_contributions"]} contributions, {data["active_days"]} active days, {len(repos)} public repositories.')


if __name__ == '__main__':
    main()
