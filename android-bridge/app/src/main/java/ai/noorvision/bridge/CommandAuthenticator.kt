package ai.noorvision.bridge

import android.content.Context
import android.util.Base64
import java.nio.charset.StandardCharsets
import java.security.MessageDigest
import javax.crypto.Mac
import javax.crypto.spec.SecretKeySpec

/**
 * Verifies short-lived, signed deep-link commands.
 * The shared secret is intentionally not hard-coded in source.
 */
class CommandAuthenticator(context: Context) {
    private val prefs = context.getSharedPreferences("noorvision_secure", Context.MODE_PRIVATE)

    fun verify(action: String, timestampSeconds: Long, nonce: String, signature: String): Boolean {
        val secret = prefs.getString(KEY_SECRET, null) ?: return false
        val now = System.currentTimeMillis() / 1000L
        if (kotlin.math.abs(now - timestampSeconds) > MAX_CLOCK_SKEW_SECONDS) return false
        if (!nonce.matches(Regex("[A-Za-z0-9_-]{16,64}"))) return false
        val payload = "$action|$timestampSeconds|$nonce"
        val expected = hmac(secret, payload)
        return MessageDigest.isEqual(expected.toByteArray(StandardCharsets.US_ASCII), signature.toByteArray(StandardCharsets.US_ASCII))
    }

    fun hasSecret(): Boolean = prefs.contains(KEY_SECRET)

    fun provisionSecret(secret: String) {
        require(secret.length >= 32) { "Secret must contain at least 32 characters" }
        prefs.edit().putString(KEY_SECRET, secret).apply()
    }

    private fun hmac(secret: String, payload: String): String {
        val mac = Mac.getInstance("HmacSHA256")
        mac.init(SecretKeySpec(secret.toByteArray(StandardCharsets.UTF_8), "HmacSHA256"))
        return Base64.encodeToString(mac.doFinal(payload.toByteArray(StandardCharsets.UTF_8)), Base64.NO_WRAP or Base64.URL_SAFE)
    }

    companion object {
        private const val KEY_SECRET = "bridge_secret"
        private const val MAX_CLOCK_SKEW_SECONDS = 60L
    }
}
