# 1    1 2 3 4 5 6 7 8 9  10 - 1
# 2    10*2 - 3 f(1)*2 - 1
# 10 12
# 21 23
# 32 34
# 43 45
# 54 56 ....
# 87 89
# 98
# 3   f(2)*2 - 2??
# 101 10X   121 123
# 210 212  232 234
# 321 323  343 345
# ...
# 876 878   89x 898
# 989 987

# 4   f(3)*2 - 2??
# 1010     1210  122
# 2101     2121  2123  232 234
# 321 323  343 345
# ...
# 876 878   89x 898
# 989 987

import sys

sys.stdin = open("Baekjoon10844.txt")
from collections import deque

a = int(input())
dp = [9, 17]
while len(dp) < a:
    # print(dp[-1] * 2 - len(dp))
    dp.append(dp[-1] * 2 - len(dp))
print(dp)
#   *2 -1   *2 - 2  *2 - 3     *2 - 8
# [9,    17,     32,    61,    116]
# 9 -0
# 9*2-1
# 17*2 -2
# 32*2 64 -3
for a in range(10):
    arr = []
    for i in range(1, 10):
        Q = deque([str(i)])
        while Q:
            n = Q.popleft()
            if len(n) < a:
                t = int(n[-1])
                if 0 <= t - 1 < 10:
                    Q.append(n + str(t - 1))
                if 0 <= t + 1 < 10:
                    Q.append(n + str(t + 1))
            elif len(n) == a:
                arr.append(n)
    print(len(arr), arr)
