class Constant:
    # fixture scopes
    FUNCTION_SCOPE: str = "function"
    CLASS_SCOPE: str = "class"
    MODULE_SCOPE: str = "module"
    PACKAGE_SCOPE: str = "package"
    SESSION_SCOPE: str = "session"

    # br types
    CHROME_BR: str = "chrome"
    FIREFOX_BR: str = "firefox"
    IE_BR: str = "ie"
    EDGE_BR: str = "edge"
    SAFARI_BR: str = "safari"
    OPERA_BR: str = "opera"
    BRAVE_BR: str = "brave"

    # timeout vars by second
    TIME_OUT_1S: int = 1
    TIME_OUT_2S: int = 2
    TIME_OUT_3S: int = 3
    TIME_OUT_5S: int = 5
    TIME_OUT_10S: int = 10
    TIME_OUT_15S: int = 15
    MIN_TIME_OUT: float = 0.5
    MAX_TIME_OUT: int = 30

    # test case statuses
    TC_PASSED_STT: str = "PASSED"
    TC_FAILED_STT: str = "FAILED"

    # function named
    FUNC_LOG_IN: str = "Log in"

    # directed urls
    LOG_IN_PATH = "login"

    # keys to press
    KEY_ENTER = "enter"
    KEY_BACKSPACE = "backspace"
    KEY_TAB = "tab"
    KEY_SHIFT = "shift"
    KEY_RETURN = "return"
    KEY_CONTROL = "control"
    KEY_LEFT_CONTROL = "left control"
    KEY_LEFT_SHIFT = "left shift"
    KEY_ALT = "alt"
    KEY_LEFT_ALT = "left alt"
    KEY_PAUSE = "pause"
    KEY_ESCAPE = "escape"
    KEY_SPACE = "space"
    KEY_PAGE_UP = "page up"
    KEY_PAGE_DOWN = "page down"
    KEY_END = "end"
    KEY_HOME = "home"
    KEY_LEFT = "left"
    KEY_UP = "up"
    KEY_RIGHT = "right"
    KEY_DOWN = "down"
    KEY_ARROW_LEFT = "arrow left"
    KEY_ARROW_UP = "arrow up"
    KEY_ARROW_RIGHT = "arrow right"
    KEY_ARROW_DOWN = "arrow down"
    KEY_INSERT = "insert"
    KEY_DELETE = "delete"
    KEY_SEMICOLON = "semicolon"
    KEY_EQUALS = "equals"
    KEY_NUMPAD_0 = "0"
    KEY_NUMPAD_1 = "1"
    KEY_NUMPAD_2 = "2"
    KEY_NUMPAD_3 = "3"
    KEY_NUMPAD_4 = "4"
    KEY_NUMPAD_5 = "5"
    KEY_NUMPAD_6 = "6"
    KEY_NUMPAD_7 = "7"
    KEY_NUMPAD_8 = "8"
    KEY_NUMPAD_9 = "9"
    KEY_MULTIPLY = "multiply"
    KEY_ADD = "add"
    KEY_SEPARATOR = "separator"
    KEY_SUBTRACT = "subtract"
    KEY_DECIMAL = "decimal"
    KEY_DIVIDE = "divide"
    KEY_F1 = "f1"
    KEY_F2 = "f2"
    KEY_F3 = "f3"
    KEY_F4 = "f4"
    KEY_F5 = "f5"
    KEY_F6 = "f6"
    KEY_F7 = "f7"
    KEY_F8 = "f8"
    KEY_F9 = "f9"
    KEY_F10 = "f10"
    KEY_F11 = "f11"
    KEY_F12 = "f12"
    # META = "meta"
    # COMMAND = "command"
    # ZENKAKU_HANKAKU = "zenkaku_hankaku"
