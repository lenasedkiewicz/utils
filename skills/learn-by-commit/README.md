# learn-by-commit

A [Claude Code skill](https://docs.claude.com/en/docs/claude-code/skills) for repositories you build in order to learn, for example to prepare for interviews. Work is done in small chunks, one chunk per commit, and for each chunk Claude:

1. **Briefs** you before writing code: what will change, how it fits the project plan and general engineering practice, and the proposed commit message.
2. **Implements** the change and runs the relevant checks.
3. **Writes a dev-journal entry** in `docs/dev-journal/NNN-<slug>.md` with the commands used, verified "Read more" links, and a quiz (revision questions plus interview-style "defend the decision" questions).
4. **Commits** the code and the journal entry together, after you approve the message.

It also keeps a cumulative `docs/commands.md` reference and saves answers to concept questions asked in chat as notes in `docs/concepts/`.

Everything learner-specific (target role, background, stack, plan file, shell, language) comes from `docs/learning-profile.md` in the target repo. If that file is missing, the skill asks a few questions and creates it from [`profile-template.md`](profile-template.md).

## Install

Copy this folder to one of:

- `~/.claude/skills/learn-by-commit/` to make it available in all your projects, or
- `<project>/.claude/skills/learn-by-commit/` to enable it for a single repository.
