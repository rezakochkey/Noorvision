package ai.noorvision.bridge

import android.content.Intent
import android.os.Bundle
import android.provider.Settings
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        findViewById<Button>(R.id.openAccessibility).setOnClickListener {
            startActivity(Intent(Settings.ACTION_ACCESSIBILITY_SETTINGS))
        }
        findViewById<Button>(R.id.openCamera).setOnClickListener {
            runCatching { startActivity(Intent("android.media.action.IMAGE_CAPTURE")) }
        }
        findViewById<Button>(R.id.goHome).setOnClickListener {
            // Global HOME requires the Accessibility Service to be enabled.
            val service = NoorAccessibilityServiceHolder.instance
            if (service == null) {
                findViewById<TextView>(R.id.status).text = "Accessibility فعال نیست."
            } else {
                service.goHome()
            }
        }
    }
}

object NoorAccessibilityServiceHolder {
    var instance: NoorAccessibilityService? = null
}
