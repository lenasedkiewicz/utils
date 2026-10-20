# Scripts

Standalone scripts. Each one is a single file with no setup beyond Python.

## `monthly_commits.py`

Scans every public, non-fork repository owned by a GitHub user and lists the days (in local time) since the 1st of the current month with commits by that user on each repo's default branch. A day counts once in the total, even if you committed to several repos on it.

**Requirements:** Python 3.11+, standard library only.

**Usage:**

```sh
python script/monthly_commits.py <github-username>
```

**Example output:**

```
Days with public commits by octocat since 2026-10-01

  dotfiles                                   3 days
  utils                                      5 days

  TOTAL (distinct days)                      6 days

  01.10, 02.10, 05.10, 07.10, 10.10, 13.10
```

**Authentication (optional):** without a token the GitHub API allows 60 requests per hour, which runs out quickly if you have many repos. The script raises that to 5000 by using, in order:

1. the `GITHUB_TOKEN` environment variable, or
2. the token from the [`gh` CLI](https://cli.github.com/) if you're logged in (`gh auth login`).
