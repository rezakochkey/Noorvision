# NOORVISION Android Bridge

Minimal Android 14 bridge MVP for a future ChatGPT-controlled device workflow.

## Current scope
- Open Android camera via standard Intent.
- Navigate Home via Accessibility global action when the service is enabled.
- Navigate Back via Accessibility global action when the service is enabled.
- Accept a `noorvision://command?action=...` deep link for an allowlisted command.
- External deep-link commands always require explicit user confirmation in the app.
- No screen-content capture in MVP (`canRetrieveWindowContent=false`).
- No contacts, SMS, payments, or background network control yet.

## Target
Samsung Galaxy A04 / Android 14 / One UI.

## Security model
The command router is allowlisted. Unknown actions are rejected. The app does not embed an OpenAI API key and does not expose a network listener. Accessibility is used only for Home/Back in this MVP and does not retrieve window content.

## ChatGPT integration status
The Android-side command boundary now exists, but the ChatGPT transport is intentionally not implemented yet. A later phase must add an authenticated, least-privilege transport before any remote execution is enabled. The deep link is a local integration seam, not proof that the ChatGPT app can invoke it directly.
