package ai.noorvision.bridge

import android.accessibilityservice.AccessibilityService
import android.content.Intent
import android.view.accessibility.AccessibilityEvent

class NoorAccessibilityService : AccessibilityService() {
    override fun onServiceConnected() {
        super.onServiceConnected()
        NoorAccessibilityServiceHolder.instance = this
    }
    override fun onAccessibilityEvent(event: AccessibilityEvent?) = Unit
    override fun onInterrupt() = Unit
    override fun onDestroy() {
        NoorAccessibilityServiceHolder.instance = null
        super.onDestroy()
    }
    fun openCamera(): Boolean = runCatching {
        startActivity(Intent("android.media.action.IMAGE_CAPTURE").addFlags(Intent.FLAG_ACTIVITY_NEW_TASK))
    }.isSuccess
    fun goHome(): Boolean = performGlobalAction(GLOBAL_ACTION_HOME)
    fun goBack(): Boolean = performGlobalAction(GLOBAL_ACTION_BACK)
}
