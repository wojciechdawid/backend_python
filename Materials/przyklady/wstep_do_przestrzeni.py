a = 1
b = 2


def foo():
    global a
    a = 2
    print("przestrzen funkcji", a, b)


foo()
print("globalna przestrzen", a, b)


a = 10


def foo():
    global a
    a = a + 2
    return a + 2


a = 10


def foo(a):
    return a + 2


a = foo(a)
