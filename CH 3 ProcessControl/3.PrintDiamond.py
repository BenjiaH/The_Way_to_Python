# 用控制台打印菱形
'''
    *			4
   * *			3
  *   *			2
 *     *		1
*       *
 *     *		0 1 5
  *   *			1 2 3
   * *			2 3 1
	* 			3 4 0
'''

N = 5
for i in range(N):
    if i == 0:
        print((N - 1 - i) * " " + "*")
    else:
        s = (N - 1 - i) * " " + "*" + (i * 2 - 1) * " " + "*"
        print(s)

for i in range(N - 1):
    if i == N - 2:
        print((i + 1) * " " + "*")
    else:
        s = (i + 1) * " " + "*" + ((N - 2 - i) * 2 - 1) * " " + "*"
        print(s)
