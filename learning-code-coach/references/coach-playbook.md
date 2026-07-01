# Learning Code Coach Playbook

## Calibration Questions

Ask only the questions needed for the current task. Prefer two questions; use four only when the user asks to configure the skill.

1. "What level should I assume: beginner, junior, mid, senior, or non-developer?"
2. "Do you want quick intuition, a practical working model, or deeper theory?"
3. "What do you most want to learn here: architecture, syntax, debugging, tests, review, product decisions, or AI collaboration?"
4. "Should I explain as we go, pause at checkpoints, or give a final walkthrough?"

Default profile when unanswered:

- Level: junior.
- Depth: practical working model.
- Style: concise notes while coding.
- Learning priority: understand the design enough to change it safely.

## Optional Profile Template

Create this only when the user explicitly asks to configure or save preferences.

```markdown
# Learning Code Coach Profile

- Level:
- Preferred depth:
- Preferred style:
- Current stack:
- Learning goals:
- Things to avoid:
```

## Explanation Templates

### Architecture

Use this for app structure, module boundaries, MVC/MVVM, Clean Architecture, services, repositories, state management, dependency injection, pipelines, infrastructure, and technical documents.

```text
Responsibility: What this part owns.
Collaborators: What it talks to.
Data flow: How information moves through the feature.
Tradeoff: Why this structure is useful and what it costs.
Change point: Where a junior should edit when a similar requirement arrives.
```

### Swift And SwiftUI

Use concrete vocabulary:

- `View`: describes UI from state; should stay mostly declarative.
- `@State`: local state owned by one view.
- `@Binding`: state passed down so a child can edit it.
- `Observable` or view model: shared state and user actions for a feature.
- Model: data shape, ideally independent from UI.
- Service/client: talks to the outside world, such as network, disk, sensors, or system APIs.
- Protocol: a boundary that makes implementations swappable and tests easier.

Junior-friendly Swift architecture note:

```text
This design keeps the screen, the feature state, and the external dependency separate.
That means the view is easier to read, the logic is easier to test, and changing the API/client later is less painful.
The cost is a little more structure up front.
```

### Web And Backend

Use concrete vocabulary:

- Component: reusable UI unit with inputs, state, and rendered output.
- Route/handler: receives a request and returns a response.
- Service: holds business logic that should not live directly in UI or route code.
- Repository/data access: isolates database details from feature logic.
- Schema/model: defines the shape and rules of the data.
- Middleware: cross-cutting behavior such as auth, logging, rate limits, or parsing.

Junior-friendly web/backend architecture note:

```text
This design separates the request layer, the feature logic, and the data layer.
That makes each part easier to test and keeps changes from spreading through the whole app.
The cost is that a simple feature may have a few more files.
```

### Data, DevOps, And Technical Artifacts

Use concrete vocabulary:

- Pipeline: ordered steps that transform input into output.
- Contract: agreed shape or behavior between two parts of a system.
- Environment: where code runs, such as local, staging, production, or CI.
- Secret: private configuration that must not be committed.
- Metric: measurement used to decide whether a change helped.
- Claim: statement in a document or AI output that needs evidence.

Junior-friendly technical artifact note:

```text
The important question is not only "does this look right?" but "what evidence would prove it?"
For code, that may be a test or build. For docs, it may be a source, example, or reproducible command.
```

### Debugging

```text
Symptom: What we observe.
Hypothesis: What might explain it.
Evidence: What logs, tests, compiler errors, traces, or screenshots show.
Fix: The smallest change that addresses the evidence.
Regression check: How we know it will not come back.
```

### AI Collaboration

Teach the learner to review AI output:

- Check whether the named APIs exist in the installed SDK or documentation.
- Ask what test would fail if the answer is wrong.
- Look for over-broad changes, hidden global state, missing error handling, and fake certainty.
- Prefer small verified changes over large untested rewrites.
- Keep product intent visible: correct code can still solve the wrong problem.

## Level Adaptation Examples

Beginner:

```text
This file decides what appears on the screen. The state is the memory the screen uses to redraw itself.
```

Junior:

```text
This is a view-model boundary. The view sends user actions into the view model, and the view model updates state. That keeps business logic out of the UI.
```

Mid-level:

```text
The useful boundary is not just MVVM; it is that persistence and networking are behind protocols, so tests can exercise feature behavior without hitting external systems.
```

Senior:

```text
The abstraction is justified if there are two implementations, a test seam, or a near-term migration. Otherwise keep the direct dependency and extract later.
```

## Micro Exercises

Offer one optional exercise only when the user wants learning mode:

- "Point to the file you would change to add a new field."
- "Predict which test should fail if this service returns an error."
- "Rename one concept in your own words."
- "Trace the data from button tap to rendered UI."

Do not include exercises in urgent production fixes unless requested.
