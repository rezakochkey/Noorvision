# NOORVISION Android Bridge

Minimal Android 14 bridge MVP for a future ChatGPT-controlled device workflow.

## Current scope
- Open Android camera via standard Intent.
- Navigate Home via Accessibility global action when the service is enabled.
- No screen-content capture in MVP (`canRetrieveWindowContent=false`).
- No contacts, SMS, payments, or background network control yet.

## Target
Samsung Galaxy A04 / Android 14 / One UI.

## Important
The bridge does not embed an OpenAI API key. The ChatGPT command channel is intentionally not implemented in this MVP; the next phase must define an authenticated, least-privilege command transport before enabling remote execution.
