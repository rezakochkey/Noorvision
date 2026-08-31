package ai.noorvision.bridge

import android.content.Intent
import android.os.Bundle
import android.provider.Settings
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    private lateinit var status: TextView
    private val router by lazy { CommandRouter(applicationContext) }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        status = findViewById(R.id.status)

        findViewById<Button>(R.id.openAccessibility).setOnClickListener {
            startActivity(Intent(Settings.ACTION_ACCESSIBILITY_SETTINGS))
        }
        findViewById<Button>(R.id.openCamera).setOnClickListener {
            execute(NoorCommand.OPEN_CAMERA)
        }
        findViewById<Button>(R.id.goHome).setOnClickListener {
            execute(NoorCommand.GO_HOME)
        }

        handleCommandIntent(intent)
    }

    override fun onNewIntent(intent: Intent?) {
        super.onNewIntent(intent)
        setIntent(intent)
        handleCommandIntent(intent)
    }

    private fun handleCommandIntent(intent: Intent?) {
        if (intent?.action != Intent.ACTION_VIEW || intent.data?.scheme != "noorvision") return
        val command = intent.data?.getQueryParameter("action")
            ?.let(NoorCommand::fromWireName)
        if (command == null) {
            status.text = "فرمان نامعتبر یا خارج از فهرست مجاز."
            return
        }
        // External deep-link commands require an explicit in-app confirmation.
        androidx.appcompat.app.AlertDialog.Builder(this)
            .setTitle("NOORVISION")
            .setMessage("اجرای فرمان ${command.wireName}؟")
            .setNegativeButton("لغو", null)
            .setPositiveButton("اجرا") { _, _ -> execute(command) }
            .show()
    }

    private fun execute(command: NoorCommand) {
        val ok = router.execute(command)
        status.text = if (ok) "اجرا شد: ${command.wireName}" else "اجرا نشد: ${command.wireName}"
    }
}

object NoorAccessibilityServiceHolder {
    var instance: NoorAccessibilityService? = null
}
