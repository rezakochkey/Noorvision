# Architecture

This document is intentionally minimal until the product scope is defined.

## Current layers

1. `src/` — implementation
2. `tests/` — verification
3. `docs/` — architecture and decisions

## Working rules

- Keep secrets outside Git.
- Prefer small, reviewable changes.
- Develop on feature branches rather than directly on `main`.
- Add tests as behavior becomes defined.
