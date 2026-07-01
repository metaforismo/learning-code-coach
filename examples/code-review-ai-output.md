# Reviewing AI Generated Code

## User Prompt

```text
Use $learning-code-coach. Review this AI-generated code and explain what I should verify before merging it.
```

## Coached Response Shape

```text
Risk: the code uses an API that may not exist in the installed package version.

Why it matters: AI can name plausible APIs that compile nowhere.

Suggested fix: check the installed docs or type definitions, then add a test that fails if this call is wrong.

Learning note: do not only ask "does the code look clean?" Ask "what evidence proves this works in this project?"
```

## Learning Target

The learner should understand hallucinated APIs, missing tests, hidden assumptions, and evidence-based review.
