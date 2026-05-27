def test():
    return bindings.test()

def add2(x: int, y: int) -> int:
    if type(x) == type(y) and type(y) == int:
        return bindings.add2(x, y)
    else:
        raise Exception("Invalid Type")

class WindowInfo(ctypes.Structure):
    _fields_ = [
        ("width", ctypes.c_int),
        ("height", ctypes.c_int)
    ]

class Event(ctypes.Structure):
    _fields_ = [
        ("window", ctypes.c_void_p),
        ("type", ctypes.c_int),
        ("key", ctypes.c_int),
        ("mods", ctypes.c_int)
    ]

def List(t):
    class cls(ctypes.Structure):
        _fields_ = [
            ("size", ctypes.c_size_t),
            ("data", ctypes.c_void_p)
        ]

        type = t

        def array(self):
            print(self.data, self.size)
            if self.size == 0:
                return (,)
            elif self.size > 0:
                return ctypes.cast(self.data, ctypes.POINTER(t * self.size)).contents
            else:
                print(f"Illegal C++ array size: {self.size}")
    return cls

class Pos(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_double),
        ("y", ctypes.c_double)
    ]

bindings.getWindowInfo.restype = WindowInfo
def getWindowInfo(window):
    return bindings.getWindowInfo(window)

def init():
    return bindings.init()

def windowHint(hint, value):
    bindings.windowHint(hint, value)

bindings.createWindow.restype = ctypes.c_void_p
def createWindow(width, height, title):
    return ctypes.c_void_p(bindings.createWindow(width, height, title.encode()+b"\x00"))

def selectWindow(window):
    bindings.selectWindow(window)

def windowShouldClose(window):
    return bindings.windowShouldClose(window)

def getWindowSize(window):
    info = getWindowInfo(window)
    return (info.width, info.height)

bindings.pollEvents.restype = List(Event)
def pollEvents():
    return bindings.pollEvents().array()

def swapBuffers(window):
    bindings.swapBuffers(window)

bindings.getCursorPos.restype = Pos
def getCursorPos(window):
    pos = bindings.getCursorPos(window)
    return (pos.x, pos.y)

constants = [
    "EVENT_KEYDOWN",
    "EVENT_KEYUP"
]

glfwConstants = [
    "RESIZABLE",
    "VISIBLE",
    "DECORATED",
    "FOCUSED",
    "AUTO_ICONIFY",
    "FLOATING",
    "MAXIMIZED",
    "CENTER_CURSOR",
    "TRANSPARENT_FRAMEBUFFER",
    "FOCUS_ON_SHOW",
    "SCALE_TO_MONITOR",
    "SCALE_FRAMEBUFFER",
    "MOUSE_PASSTHROUGH",
    "POSITION_X",
    "POSITION_Y",
    "RED_BITS",
    "GREEN_BITS",
    "BLUE_BITS",
    "ALPHA_BITS",
    "DEPTH_BITS",
    "STENCIL_BITS",
    "ACCUM_RED_BITS",
    "ACCUM_GREEN_BITS",
    "ACCUM_BLUE_BITS",
    "ACCUM_ALPHA_BITS",
    "AUX_BUFFERS",
    "SAMPLES",
    "REFRESH_RATE",
    "STEREO",
    "SRGB_CAPABLE",
    "DOUBLEBUFFER",
    "CLIENT_API",
    "CONTEXT_CREATION_API",
    "CONTEXT_VERSION_MAJOR",
    "CONTEXT_VERSION_MINOR",
    "CONTEXT_ROBUSTNESS",
    "CONTEXT_RELEASE_BEHAVIOR",
    "OPENGL_FORWARD_COMPAT",
    "CONTEXT_DEBUG",
    "OPENGL_PROFILE",
    "WIN32_KEYBOARD_MENU",
    "WIN32_SHOWDEFAULT",
    "COCOA_FRAME_NAME",
    "COCOA_GRAPHICS_SWITCHING",
    "WAYLAND_APP_ID",
    "X11_CLASS_NAME",
    "X11_INSTANCE_NAME",

    "KEY_SPACE",
    "KEY_APOSTROPHE",
    "KEY_COMMA",
    "KEY_MINUS",
    "KEY_PERIOD",
    "KEY_SLASH",
    "KEY_0",
    "KEY_1",
    "KEY_2",
    "KEY_3",
    "KEY_4",
    "KEY_9",
    "KEY_SEMICOLON",
    "KEY_EQUAL",
    "KEY_A",
    "KEY_B",
    "KEY_C",
    "KEY_D",
    "KEY_E",
    "KEY_F",
    "KEY_G",
    "KEY_H",
    "KEY_I",
    "KEY_J",
    "KEY_K",
    "KEY_L",
    "KEY_M",
    "KEY_N",
    "KEY_O",
    "KEY_P",
    "KEY_Q",
    "KEY_R",
    "KEY_S",
    "KEY_T",
    "KEY_U",
    "KEY_V",
    "KEY_W",
    "KEY_X",
    "KEY_Y",
    "KEY_Z",
    "KEY_LEFT_BRACKET",
    "KEY_BACKSLASH",
    "KEY_RIGHT_BRACKET",
    "KEY_GRAVE_ACCENT",
    "KEY_WORLD_1",
    "KEY_WORLD_2",
    "KEY_ESCAPE",
    "KEY_ENTER",
    "KEY_TAB",
    "KEY_BACKSPACE",
    "KEY_INSERT",
    "KEY_DELETE",
    "KEY_RIGHT",
    "KEY_LEFT",
    "KEY_DOWN",
    "KEY_UP",
    "KEY_PAGE_UP",
    "KEY_PAGE_DOWN",
    "KEY_HOME",
    "KEY_END",
    "KEY_CAPS_LOCK",
    "KEY_SCROLL_LOCK",
    "KEY_NUM_LOCK",
    "KEY_PRINT_SCREEN",
    "KEY_PAUSE",
    "KEY_F1",
    "KEY_F2",
    "KEY_F3",
    "KEY_F4",
    "KEY_F5",
    "KEY_F6",
    "KEY_F7",
    "KEY_F8",
    "KEY_F9",
    "KEY_F10",
    "KEY_F11",
    "KEY_F12",
    "KEY_F13",
    "KEY_F14",
    "KEY_F15",
    "KEY_F16",
    "KEY_F17",
    "KEY_F18",
    "KEY_F19",
    "KEY_F20",
    "KEY_F21",
    "KEY_F22",
    "KEY_F23",
    "KEY_F24",
    "KEY_F25",
    "KEY_KP_0",
    "KEY_KP_1",
    "KEY_KP_2",
    "KEY_KP_3",
    "KEY_KP_4",
    "KEY_KP_5",
    "KEY_KP_6",
    "KEY_KP_7",
    "KEY_KP_8",
    "KEY_KP_9",
    "KEY_KP_DECIMAL",
    "KEY_KP_DIVIDE",
    "KEY_KP_MULTIPLY",
    "KEY_KP_SUBTRACT",
    "KEY_KP_ADD",
    "KEY_KP_ENTER",
    "KEY_KP_EQUAL",
    "KEY_LEFT_SHIFT",
    "KEY_LEFT_CONTROL",
    "KEY_LEFT_ALT",
    "KEY_LEFT_SUPER",
    "KEY_RIGHT_SHIFT",
    "KEY_RIGHT_CONTROL",
    "KEY_RIGHT_ALT",
    "KEY_RIGHT_SUPER",
    "KEY_MENU",
    "KEY_LAST",

    "MOD_SHIFT",
    "MOD_CONTROL",
    "MOD_ALT",
    "MOD_SUPER",
    "MOD_CAPS_LOCK",
    "MOD_NUM_LOCK",

    "MOUSE_BUTTON_1",
    "MOUSE_BUTTON_2",
    "MOUSE_BUTTON_3",
    "MOUSE_BUTTON_4",
    "MOUSE_BUTTON_5",
    "MOUSE_BUTTON_6",
    "MOUSE_BUTTON_7",
    "MOUSE_BUTTON_8",
    "MOUSE_BUTTON_LAST",
    "MOUSE_BUTTON_LEFT",
    "MOUSE_BUTTON_RIGHT",
    "MOUSE_BUTTON_MIDDLE"
]

for constant in constants:
    globals()[constant] = ctypes.c_int.in_dll(bindings, constant).value
for constant in glfwConstants:
    globals()[constant] = ctypes.c_int.in_dll(bindings, "VAR_GLFW_" + constant).value
del constants
del glfwConstants
del constant
