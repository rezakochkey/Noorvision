package ai.noorvision.bridge

enum class NoorCommand(val wireName: String) {
    OPEN_CAMERA("OPEN_CAMERA"),
    GO_HOME("GO_HOME"),
    GO_BACK("GO_BACK");

    companion object {
        fun fromWireName(value: String): NoorCommand? = entries.firstOrNull { it.wireName == value }
    }
}
