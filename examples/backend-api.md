# Backend API Endpoint

## User Prompt

```text
Use $learning-code-coach. Add a backend endpoint for creating a project and explain why the code is split across files.
```

## Coached Response Shape

```text
Change: I added a route, a service, and a repository call.

Why: the route handles HTTP details. The service owns the business rule. The repository owns database access.

Tradeoff: this is more structure than putting everything in one file, but it is easier to test and safer to change later.

Regression check: the endpoint should have a test for success, validation failure, and database failure.
```

## Learning Target

The learner should understand request layer, feature logic, data access, and why tests map to those boundaries.
