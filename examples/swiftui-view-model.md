# SwiftUI View Model

## User Prompt

```text
Use $learning-code-coach. I am building a SwiftUI screen. Explain why this view model exists and when it is worth adding.
```

## Coached Response Shape

```text
Responsibility: the view describes the screen. The view model owns loading, user actions, and state transitions.

Data flow: the button calls the view model. The view model updates state. SwiftUI redraws the view from that state.

Tradeoff: a view model adds another file. It is useful when the screen has async work, validation, navigation decisions, or logic you want to test.

What would break first: if the API fails and error state is not modeled, the view may show stale or empty data.
```

## Learning Target

The learner should understand view, state, view model, async work, and testable feature logic.
