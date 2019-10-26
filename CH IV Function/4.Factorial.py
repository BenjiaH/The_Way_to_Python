def fact(N):
    if N < 1:
        print("ERROR!")
    elif N == 1:
        return 1
    else:
        return fact(N - 1) * N


print(fact(int(input("Enter a number:"))))