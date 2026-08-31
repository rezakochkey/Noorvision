# NOORVISION Pairing v1

## User flow
1. Open NOORVISION Bridge on the phone.
2. Tap **Pair a controller**.
3. The bridge creates a short-lived pairing session and a random secret.
4. The phone displays a one-time code/QR payload.
5. The controller proves possession of the pairing material.
6. The bridge stores the resulting secret using Android Keystore protection.
7. The pairing session expires immediately after success or after its short timeout.

## Constraints
- Pairing must happen locally and intentionally; there is no unauthenticated remote enrollment.
- Pairing codes are single-use and short-lived.
- The bridge never logs the raw secret.
- Revoke-all is available from the bridge settings.
- Before production remote transport is selected, commands are injected locally for testing.

## Test commands
The first device test should exercise `OPEN_CAMERA`, `GO_HOME`, and `GO_BACK`. `MAKE_CALL` remains confirmation-gated.
