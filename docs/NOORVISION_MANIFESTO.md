# Noorvision — Project Manifesto

## Purpose

This repository is the engineering home for Noorvision. Its purpose is to provide a durable, inspectable place for ideas, experiments, software, documentation, and decisions that may grow into useful tools.

## Operating principles

1. **Build before boasting.** Claims should be backed by working artifacts.
2. **Keep the system inspectable.** Important behavior and decisions should be documented.
3. **Prefer reversible steps.** Work on branches, test changes, and preserve a clean main branch.
4. **Protect secrets.** Credentials, tokens, private keys, and authentication codes never belong in source control.
5. **Human benefit first.** Technology is a means; usefulness, reliability, and safety are the measures of success.
6. **Small steps, compounding capability.** Start simple and add complexity only when it earns its place.

## What belongs here

- Source code and prototypes
- Architecture and technical decisions
- Experiments and research notes
- Tests and reproducible examples
- Documentation for future maintainers

## What does not belong here

- Passwords, API keys, private tokens, seed phrases, or 2FA codes
- Unreviewed personal data
- Irreversible production actions without an explicit operational reason
- Empty complexity added merely to make the project look sophisticated

## Current state

Noorvision is in the initial scaffold stage. The product scope is intentionally open. The next stage is to define a concrete problem, a first useful capability, and a minimal implementation that can be tested end to end.
