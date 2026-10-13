"""Count the days this month on which you committed to your public repos.

Scans every public repository owned by a GitHub user and collects the days
(in local time) with commits on each repo's default branch authored by that
user since the 1st of the month. A day counts once even if you committed to
several repos on it.

Usage:
    python monthly_commits.py <github-username>

Auth (optional, but raises the rate limit from 60 to 5000 requests/hour):
    set GITHUB_TOKEN, or be logged in with the `gh` CLI.
"""

import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

API = "https://api.github.com"


def get_token():
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token
    try:
        result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
        return result.stdout.strip() or None
    except FileNotFoundError:
        return None


def get_json(url, token):
    request = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request) as response:
        return json.load(response)


def get_all_pages(url, token):
    items, page = [], 1
    while True:
        separator = "&" if "?" in url else "?"
        batch = get_json(f"{url}{separator}per_page=100&page={page}", token)
        items.extend(batch)
        if len(batch) < 100:
            return items
        page += 1


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    username = sys.argv[1]
    token = get_token()
    now = datetime.now().astimezone()
    since = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    since_iso = since.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    repos = get_all_pages(f"{API}/users/{username}/repos?type=owner", token)
    repos = [r for r in repos if not r["private"] and not r["fork"]]

    print(f"Days with public commits by {username} since {since:%Y-%m-%d}\n")
    all_days = set()
    for repo in sorted(repos, key=lambda r: r["name"].lower()):
        url = f"{API}/repos/{repo['full_name']}/commits?author={username}&since={since_iso}"
        try:
            commits = get_all_pages(url, token)
        except urllib.error.HTTPError as error:
            if error.code == 409:  # empty repository
                continue
            raise
        # Dates come back in UTC; convert to local time so days match your calendar.
        days = {
            datetime.fromisoformat(c["commit"]["author"]["date"]).astimezone().date()
            for c in commits
        }
        if days:
            print(f"  {repo['name']:<40} {len(days):>3} days")
            all_days |= days

    print(f"\n  {'TOTAL (distinct days)':<40} {len(all_days):>3} days")
    if all_days:
        print("\n  " + ", ".join(f"{day:%d.%m}" for day in sorted(all_days)))


if __name__ == "__main__":
    main()
