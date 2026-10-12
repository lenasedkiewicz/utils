---
name: learn-by-commit
description: Use for EVERY chunk of coding work in a repository that has opted into learning mode (one chunk = one commit). Explains the change before coding, relates it to the project plan and general practice, then after the change writes a dev-journal entry with verified online resources and a quiz for revision and interview-style defence of decisions. Tailored to the learner via docs/learning-profile.md.
---

# Learn by commit

The owner of this repo builds it as a way to learn, for example to prepare for interviews for a particular role. Every commit is also a lesson, and the lessons can later be imported as a learning track. Work in small chunks, where **one chunk is one commit**. Follow the steps below for every chunk, in order. The user may approve tool calls manually, so the explanation must come before the code.

## 0. Learner profile (read first)

Everything learner-specific comes from **`docs/learning-profile.md`**. Read it at the start of each session. If it doesn't exist, ask the user the questions below once, create it from `profile-template.md` (next to this skill), and commit it as `docs: add learning profile`.

| Field | Used for |
|---|---|
| **Goal** – target role(s) and level, e.g. "junior backend developer", "mid data engineer", "QA automation", or "just learning" | Pitch of explanations, quiz difficulty, "Defend the decision" framing |
| **Background** – what the learner already knows | What to skip vs. explain from scratch |
| **Project** – name and one-line description | Grounding examples ("where it fits in <project>") |
| **Plan file** – path and how items are identified (e.g. `plan.md`, milestones A–D) | Section 1b and the journal `milestone` field |
| **Stack** – languages, frameworks, tools | Choosing relevant sources and concepts |
| **Shells / OS** – e.g. bash on macOS, PowerShell on Windows | Command explanations and equivalents |
| **Language** – language for journal and quiz | All written output |
| **Preferred sources** – optional additions or exclusions | "Read more" links |
| **Quiz mix** – optional, default ⅓ easier / ⅔ at target level | Quiz difficulty |

Below, `<goal>`, `<project>`, `<plan>` etc. refer to these fields. If the profile has no plan file, skip the plan-related parts and say so.

## 1. Before coding: the briefing (in chat, before any edit)

Write a short briefing with these three headings:

**a) What we're doing**
- The goal of this chunk in 2–4 sentences.
- The files that will be created or changed, with one line each on why.
- Name any new dependency and say why it was chosen over the obvious alternative.

**b) How it fits**
- *In the plan:* which item in `<plan>` this chunk delivers. Say what it unblocks next.
- *In general practice:* the engineering principle or pattern behind it. Examples: separation of concerns, pure functions, schema migrations, idempotency, test pyramid, conventional commits. Explain it in plain words at the learner's level, and say when you would *not* do it this way.

**c) Commit**
- The proposed commit message, in Conventional Commits format (`feat:`, `fix:`, `test:`, `chore:`, `docs:`, `refactor:`).

Keep the briefing tight, at roughly one screen. If the chunk turns out to be too big for one logically connected commit, propose splitting it.

## 2. Code

Implement only what the briefing describes. When you make a decision the briefing didn't foresee, say so in one line as you go. Run the relevant tests, lint or typecheck before the commit, and report the result honestly.

## 3. Dev-journal entry (part of the same commit)

Create `docs/dev-journal/NNN-<kebab-slug>.md`. `NNN` is the next free three-digit number. Use this template:

```markdown
---
id: NNN
title: <chunk title>
commit: "<commit message subject>"
plan-item: <plan item id and name, or "none">
date: <YYYY-MM-DD>
tags: [<topics, e.g. sqlite, migrations, testing>]
---

# <chunk title>

## What we did
<what changed and why, 1–2 short paragraphs; reference key files as `path:line`>

## How it fits
- **Plan:** <plan item, what it unblocks>
- **Practice:** <the principle(s), trade-offs, when you'd choose differently>

## Commands used
- `<command --flags>` — <what it was for in this chunk>
<every command run; explanations live in docs/commands.md>

## Read more
- [<title>](<url>) — <source> · <one line: what to take from it>
<3–6 links>

## Quiz

### Revise
1. <question checking understanding of a concept>
   <details><summary>Answer</summary>

   <answer, 1–4 sentences>
   </details>
<4–6 questions, mixed: multiple choice (list options a–d), short answer, "what does this code do", "spot the bug">

### Defend the decision
1. <interview-style question about a decision made in THIS commit, e.g. "Why an append-only ledger instead of a balance column?">
   <details><summary>Model answer</summary>

   <answer naming the trade-offs and the alternative>
   </details>
<2–4 questions>
```

### Commands used (journal section plus `docs/commands.md`)

Add a `## Commands used` section to the entry, between "How it fits" and "Read more". List every shell command run for this chunk, including setup, debugging and verification, with the exact flags. One line each: `` `command --flags` `` and what it was for here. Then update **`docs/commands.md`**, the cumulative reference (create it if missing, with sections by tool, e.g. Git, package manager, filesystem):
- Any command or flag **not yet explained** there gets an entry in the right section: syntax, what it does, each flag, a repo example, an equivalent for each other shell listed in the profile where it differs, and `*First used in NNN*`.
- A command already explained but used with a **new flag** gets that flag added to its entry.
- Don't explain anything twice. Link instead, for example `see [mkdir](../commands.md#mkdir-make-a-directory)`.
- Flag destructive commands (`rm -rf`, `git reset --hard`, `--force`) with ⚠️ and say when they're safe.

### Rules for "Read more"
- Prefer high-quality sources for the profile's stack: official documentation for the tools used, plus general sources such as MDN, freeCodeCamp, web.dev, martinfowler.com, roadmap.sh, Refactoring Guru, The Odin Project and conventionalcommits.org. Respect the profile's preferred or excluded sources.
- Use WebSearch to find each link, then **check it with WebFetch** before including it. Never include a URL you haven't fetched successfully. If none can be verified, say so instead of inventing one.
- Include at least one beginner-friendly link and at least one deeper or official link per entry.
- Links must match the concepts in *this* commit, not generic tutorials.

### Rules for the quiz
- Questions must be answerable from this commit's code plus the linked reading.
- "Defend the decision" questions must reference the actual choices in this repo, framed the way an interviewer for `<goal>` would ask them, so the learner can talk about the project in an interview. If the goal isn't interview-related, frame them as a code reviewer would.
- Use the profile's quiz mix; by default roughly a third below the target level and the rest at it.

## 4. Commit

Stage the code and the journal entry together, then show the user the final commit message for approval. Never push unless asked. After committing, finish with a one-line summary and the path to the journal entry. Do not repeat the quiz in chat.

## Concept notes (questions asked in chat)

When the user asks a concept question such as "what is an ORM?" or "why X over Y?", whether during a chunk or between chunks, answer in chat first. Then save the answer as a concept note:

- Create `docs/concepts/NNN-<kebab-slug>.md`. `NNN` is the next free three-digit number in `docs/concepts/`, counted separately from the dev-journal numbers. Refer to notes as `concept NNN`.
- Use this frontmatter:
  ```markdown
  ---
  id: NNN
  title: <concept>
  date: <YYYY-MM-DD>
  asked-during: <dev-journal id or commit subject in progress, or "between commits">
  tags: [<topics>]
  ---
  ```
- The body holds the chat explanation, tidied: what it is, where it fits in `<project>`, alternatives and trade-offs, and a short "interview answer" pitched at `<goal>`. End with a **Read more** section that follows the same link rules as the dev-journal: every link is checked with WebFetch.
- Add one line to `docs/concepts/README.md` in the form `- NNN · YYYY-MM-DD · [Title](NNN-slug.md): one-line hook`.
- If the topic already has a note, update that note and its `date` instead of making a new one.
- Commit the note with the current chunk. If no chunk is in progress, use a separate `docs:` commit, which needs no journal entry.
- When a dev-journal entry touches a concept that has a note, link to the note under **Read more**.

## Exceptions

For trivial chunks (a typo, a formatting-only change, a dependency bump), skip the journal and say so in the briefing.
