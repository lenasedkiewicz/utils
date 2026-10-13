# utils

A small collection of personal utilities: standalone scripts and Claude Code skills.

## Contents

| Path | What it is |
|---|---|
| [`script/monthly_commits.py`](script/monthly_commits.py) | Counts the days this month on which you committed to your public GitHub repos |
| [`skills/learn-by-commit/`](skills/learn-by-commit/) | Claude Code skill that turns every commit into a lesson: briefing, dev-journal entry, reading list and quiz |

## Scripts

### `monthly_commits.py`

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

## Skills

### `learn-by-commit`

A [Claude Code skill](https://docs.claude.com/en/docs/claude-code/skills) for repositories you build in order to learn, for example to prepare for interviews. Work is done in small chunks, one chunk per commit, and for each chunk Claude:

1. **Briefs** you before writing code: what will change, how it fits the project plan and general engineering practice, and the proposed commit message.
2. **Implements** the change and runs the relevant checks.
3. **Writes a dev-journal entry** in `docs/dev-journal/NNN-<slug>.md` with the commands used, verified "Read more" links, and a quiz (revision questions plus interview-style "defend the decision" questions).
4. **Commits** the code and the journal entry together, after you approve the message.

It also keeps a cumulative `docs/commands.md` reference and saves answers to concept questions asked in chat as notes in `docs/concepts/`.

Everything learner-specific (target role, background, stack, plan file, shell, language) comes from `docs/learning-profile.md` in the target repo. If that file is missing, the skill asks a few questions and creates it from [`profile-template.md`](skills/learn-by-commit/profile-template.md).

**Install** by copying the skill folder to one of:

- `~/.claude/skills/learn-by-commit/` to make it available in all your projects, or
- `<project>/.claude/skills/learn-by-commit/` to enable it for a single repository.
