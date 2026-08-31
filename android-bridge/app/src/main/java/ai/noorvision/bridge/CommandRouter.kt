package ai.noorvision.bridge

import android.content.Context
import android.content.Intent

class CommandRouter(private val context: Context) {
    fun execute(command: NoorCommand): Boolean = when (command) {
        NoorCommand.OPEN_CAMERA -> runCatching {
            context.startActivity(
                Intent("android.media.action.IMAGE_CAPTURE")
                    .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
            )
        }.isSuccess
        NoorCommand.GO_HOME -> NoorAccessibilityServiceHolder.instance?.goHome() == true
        NoorCommand.GO_BACK -> NoorAccessibilityServiceHolder.instance?.goBack() == true
    }
}
