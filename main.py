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

def pollEvents():
    bindings.pollEvents()

def swapBuffers(window):
    bindings.swapBuffers(window)

constants = [
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
    "X11_INSTANCE_NAME"
]

for constant in constants:
    globals()[constant] = ctypes.c_int.in_dll(bindings, "VAR_GLFW_" + constant).value
del constant
del constants
