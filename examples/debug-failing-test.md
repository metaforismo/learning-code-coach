# Debugging A Failing Test

## User Prompt

```text
Use $learning-code-coach. This test fails after an AI-generated change. Fix it and teach me how to debug it.
```

## Coached Response Shape

```text
Symptom: the test expected one saved item, but the result has zero.

Hypothesis: the new validation rejects the input before saving.

Evidence: the failing path returns a validation error and never calls the repository.

Fix: update the test input to include the required field, or change the validation if the field should be optional.

Regression test: keep one test for valid input and one test for the missing field.
```

## Learning Target

The learner should learn to move from symptom to hypothesis to evidence, instead of guessing from the error message alone.
