# Security Policy

## Reporting

Please report security issues privately through GitHub security advisories when available, or by contacting the maintainer through the repository owner profile.

Do not open a public issue for vulnerabilities involving credential leakage, unsafe installation instructions, prompt-injection risks, or hidden persistence behavior.

## Scope

This repository contains a Codex skill and a lightweight validation script. Security-sensitive areas include:

- installation instructions;
- learner profile persistence;
- prompt-injection-prone guidance;
- CI configuration;
- accidental inclusion of secrets or private project paths.

## Expectations

The skill must not ask agents to silently store personal learner profiles. Any persisted profile should be explicit, short, and user-approved.
