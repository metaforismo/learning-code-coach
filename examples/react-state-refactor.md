# React State And Component Boundary

## User Prompt

```text
Use $learning-code-coach. I have a React component with too much state. Refactor it and explain the architecture like I am a junior developer.
```

## Coached Response Shape

```text
Change: I moved the form state into a small hook and kept the component focused on rendering.

Why: a component is easier to read when it answers one question: what should the user see? The hook owns the state changes.

How to recognize this later: when a component has many handlers, repeated validation logic, or state updates that hide the UI structure, look for a hook boundary.

Quick check: if validation rules change, should you edit the component markup or the hook?
```

## Learning Target

The learner should understand the difference between UI rendering, local state, and reusable feature logic.
