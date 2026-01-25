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
