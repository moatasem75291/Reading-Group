def a():
    print("a() stars")
    b()
    d()
    print("a() returns")


def b():
    print("b() stars")
    c()
    print("b() returns")


def c():
    print("c() stars")
    print("c() returns")


def d():
    print("d() stars")
    print("d() returns")


a()
