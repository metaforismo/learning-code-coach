# Installation And Learner Profile

Learning Code Coach is packaged as a Codex skill, but the method is general. It is a reusable coaching prompt for AI-assisted technical work.

## Install As A Codex Skill

From this repository:

```bash
cp -R learning-code-coach "${CODEX_HOME:-$HOME/.codex}/skills/"
```

From a release zip:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
unzip learning-code-coach-v0.2.0.zip -d "${CODEX_HOME:-$HOME/.codex}/skills"
```

Then ask:

```text
Use $learning-code-coach. I am a junior developer. Help me build this feature and explain the important choices.
```

## Use With Other Assistants

If your assistant does not support Codex skills, copy the contents of `learning-code-coach/SKILL.md` into a reusable custom instruction or project instruction. When a task needs deeper examples, also copy the relevant parts of `learning-code-coach/references/coach-playbook.md`.

## Configure A Learner Profile

The coach should not store personal learning data silently. If you want a saved profile, ask for it directly:

```text
Use $learning-code-coach and create a learner profile for this project.
```

Suggested profile:

```markdown
# Learning Code Coach Profile

- Level: junior
- Preferred depth: practical working model
- Preferred style: concise notes while coding
- Current stack: React, Node, PostgreSQL
- Learning goals: architecture, tests, debugging
- Things to avoid: long theory before code
```

## Calibration Questions

The assistant may ask:

1. What level should I assume?
2. Do you want quick intuition, a practical working model, or deeper theory?
3. What do you most want to learn here?
4. Should I explain as we go, pause at checkpoints, or give a final walkthrough?

If you do not answer, the default is junior level, practical working model, and short notes while building.
