def test():
    return bindings.test()


def add2(x: int, y: int) -> int:
    if type(x) == type(y) and type(y) == int:
        return bindings.add2(x, y)
    else:
        raise Exception("Invalid Type")
