import functools


def fn(x, y):
    return x * y


def factorial(n):
    # r = 1
    if n < 1:
        print("n不能小于1")
        return
    else:
        return functools.reduce(fn, range(1, n + 1))
        return functools.reduce


print(factorial(5))
