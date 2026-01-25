def test():
    return bindings.test()


def add2(x: int, y: int) -> int:
    if type(x) == type(y) and type(y) == int:
        return bindings.add2(x, y)
    else:
        raise Exception("Invalid Type")

def init():
    return bindings.init()

def createWindow(width, height):
    return bindings.createWindow(width, height)

def windowShouldClose():
    return bindings.windowShouldClose()

def pollEvents():
    bindings.pollEvents()

def swapBuffers():
    bindings.swapBuffers()

constants =
[
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
    "POSITION_Y"
]

for constant in constants:
    globals()[constant] = bindings.__dict__["GLFW_" + constant]
del constants
