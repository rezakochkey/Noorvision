# NOORVISION Android Bridge — Secure Command Channel v2

## Goal
Provide a secure, explicit command boundary between an authorized controller and the Android bridge. The bridge executes only an allowlisted command set and never exposes an unauthenticated listening port.

## Security model
- Pairing is explicit and user initiated.
- A 256-bit random bridge secret is generated on-device and protected by Android Keystore.
- Every command carries `id`, `action`, `issued_at`, `nonce`, and `signature`.
- Signature: HMAC-SHA256 over the canonical UTF-8 representation of `id|action|issued_at|nonce|payload`.
- Reject commands with invalid signatures, stale timestamps, reused nonces, unknown actions, or malformed payloads.
- Sensitive actions require local user confirmation.
- No OpenAI API key is stored in the Android app.
- No command endpoint is exposed to the public Internet.

## Transport boundary
The Android app is the execution endpoint. A future controller adapter may deliver commands through an authenticated, encrypted transport. Transport credentials are separate from the bridge secret. The MVP does not assume that the ChatGPT Android app can directly call arbitrary localhost endpoints.

## Allowlist v0.2
- `OPEN_CAMERA`
- `OPEN_APP` (package name only)
- `GO_HOME`
- `GO_BACK`
- `MAKE_CALL` (explicit confirmation required)

## Execution policy
Prefer Android public APIs/Intents for camera, app launch, and calling. Accessibility is a fallback for UI actions that have no suitable public API and must be enabled manually by the device owner.

## Next implementation step
Add a local pairing screen that displays a one-time pairing code/QR payload and binds the controller to the device. Then add a test-only command injector inside the app so the command router can be verified on a real Android 14 device before any remote transport is introduced.
