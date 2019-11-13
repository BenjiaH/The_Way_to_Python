N = input("请输入N:")

if N == "":
    N = 6

N = int(N)
# N = 6
array = [[0] * N]  # [[0, 0, 0, 0, 0....]]
for i in range(N - 1):
    array += [[0] * N]

# 控制方向
# 0代表向下，1代表向右，2代表向左，3代表向上
orient = 0
j, k = 0, 0
for i in range(1, N ** 2 + 1):
    array[j][k] = i
    if j + k == N - 1:
        if j > k:
            orient = 1
        else:
            orient = 2
    elif j == k and j >= N / 2:
        orient = 3
    elif j + 1 == k and k <= N / 2:
        orient = 0

    if orient == 0:
        j += 1
    if orient == 1:
        k += 1
    if orient == 2:
        k -= 1
    if orient == 3:
        j -= 1

for ele in array:
    for e in ele:
        print("%02d" % e, end=" ")
    print("")
