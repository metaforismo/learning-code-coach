# Learning Code Coach

Learning Code Coach is a Codex skill for learning while building. It helps an agent complete real technical work while explaining the important implementation choices at the learner's level.

The main use case is coding, especially for junior developers using AI-assisted tools. The skill is intentionally broader than one stack: it can coach through frontend, backend, mobile, data, DevOps, technical writing, reviews, debugging, tests, architecture, and AI-generated artifacts.

## Why This Exists

AI can write a lot of code quickly, but speed alone does not teach the developer how to maintain, debug, or safely extend that code later. This skill makes the assistant act less like a black-box generator and more like a practical mentor:

- ask a few calibration questions when helpful;
- explain only the concepts that matter for the current task;
- connect explanations to the actual files and decisions;
- point out common AI failure modes;
- finish with a short recap and a next learning step.

## Installation

Copy the skill folder into your Codex skills directory:

```bash
cp -R learning-code-coach "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Then invoke it explicitly:

```text
Use $learning-code-coach to help me build this feature while explaining the architecture at my level.
```

Codex may also invoke it implicitly when the user asks for mentoring, junior-friendly explanations, learning while building, architecture explanations, or a learner profile.

## Example Prompts

```text
Use $learning-code-coach. I am a junior developer. Help me add this API endpoint and explain the architecture as we go.
```

```text
Use $learning-code-coach to review this AI-generated React code and teach me what to verify before merging it.
```

```text
Use $learning-code-coach. I am writing a SwiftUI app and want to understand why this view model exists.
```

```text
Use $learning-code-coach to help me improve this deployment workflow and explain the CI/CD concepts simply.
```

## Repository Layout

```text
learning-code-coach/
  SKILL.md
  agents/openai.yaml
  references/coach-playbook.md
scripts/
  validate_skill.py
```

## Validation

Run the repository validation script:

```bash
python3 scripts/validate_skill.py
```

The script checks the skill frontmatter, metadata, required references, and placeholder-free content without requiring third-party dependencies.

## Project Posture

This is a small educational skill, not a replacement for tests, documentation, code review, or real mentorship. Its goal is to make AI-assisted work more legible and less passive.
