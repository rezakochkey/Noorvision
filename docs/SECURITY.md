# Noorvision Security Policy

## Core rule

Secrets must never be committed to this repository.

Do not store:

- passwords
- API keys
- access tokens
- private keys
- seed phrases
- 2FA or verification codes
- production credentials

Use environment variables or an appropriate secret-management system instead.

## Development hygiene

- Work on feature branches.
- Review changes before merging to `main`.
- Keep dependencies minimal and current.
- Do not paste sensitive credentials into issues, commits, documentation, or chat.
- Treat unexpected permissions or authentication prompts as security events and verify them before proceeding.

## Incident response

If a secret is accidentally committed, assume it is compromised. Revoke or rotate it immediately, then remove it from the repository history using an appropriate repository-history cleanup process.

## Scope

This policy is intentionally simple while Noorvision is in its foundation stage. It should be expanded when the project begins handling real user data, external services, or production infrastructure.
