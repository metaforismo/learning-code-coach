# Learning Code Coach

Learning Code Coach is a small instruction pack for learning while building with AI. It helps an AI assistant finish real technical work while also explaining the important choices at the learner's level.

The main use case is coding, especially for junior developers. It is not tied to one stack or one tool. It can coach through frontend, backend, mobile, data, DevOps, technical writing, reviews, debugging, tests, architecture, and AI-generated artifacts.

## Why This Exists

In the last few months, AI has started to write more and more of the code people ship. It also writes docs, tests, plans, reviews, and scripts. That is powerful, but it creates a real learning risk: a junior developer can receive working code without understanding how to maintain it, debug it, or safely extend it later.

Learning Code Coach makes the assistant act less like a black-box generator and more like a practical mentor:

- ask a few calibration questions when helpful;
- explain only the concepts that matter for the current task;
- connect explanations to the actual files and decisions;
- point out common AI failure modes;
- finish with a short recap and a next learning step.

## Installation

This repository ships the coach in Codex skill format, but the coaching method is general. You can also copy the instructions into another AI assistant that supports reusable system prompts or custom instructions.

To install it as a Codex skill, copy the skill folder into your skills directory:

```bash
cp -R learning-code-coach "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Then invoke it explicitly:

```text
Use $learning-code-coach to help me build this feature while explaining the architecture at my level.
```

The assistant may also invoke it implicitly when the user asks for mentoring, junior-friendly explanations, learning while building, architecture explanations, or a learner profile.

For a fuller setup flow, see [Installation And Learner Profile](docs/installation-and-profile.md).

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

## Demo

Without a coach:

```text
I added a service and a route for the new endpoint.
```

With Learning Code Coach:

```text
I added a route for the HTTP request and a service for the feature logic.

Why this shape matters: the route should stay small. It reads the request and sends the response. The service owns the business rule. Later, if the rule changes, you know where to edit.

Quick check: if this endpoint starts returning the wrong data, which file would you inspect first?
```

## Real Use Cases

- [React state and component boundary](examples/react-state-refactor.md)
- [Backend API endpoint](examples/backend-api.md)
- [SwiftUI view model](examples/swiftui-view-model.md)
- [Debugging a failing test](examples/debug-failing-test.md)
- [Reviewing AI-generated code](examples/code-review-ai-output.md)

## Repository Layout

```text
learning-code-coach/
  SKILL.md
  agents/openai.yaml
  references/coach-playbook.md
docs/
  installation-and-profile.md
examples/
  backend-api.md
  code-review-ai-output.md
  debug-failing-test.md
  react-state-refactor.md
  swiftui-view-model.md
scripts/
  build_release_zip.py
  validate_skill.py
tests/
  test_skill_quality.py
```

## Validation

Run the repository validation and quality tests:

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests
```

The checks validate the skill structure, metadata, required references, examples, installation guide, and text-quality rules without requiring third-party dependencies.

## Release Zip

Build an installable zip:

```bash
python3 scripts/build_release_zip.py v0.2.0
```

The zip contains the `learning-code-coach` skill folder at the root, so users can unzip it directly into their skills directory.

## Project Posture

This is a small educational skill, not a replacement for tests, documentation, code review, or real mentorship. Its goal is to make AI-assisted work more legible and less passive.
