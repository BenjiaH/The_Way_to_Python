def factorial(n):
    # r = 1
    if n < 1:
        print("n不能小于1")
        return
    elif n == 1:
        return 1
    else:
        # for i in range(1, n + 1):
        # r *= i
        # return r
        return factorial(n - 1) * n


print(factorial(5))