import sys

sys.stdin = open("Baekjoon9095.txt")


# 0          0
# 0

# 1          1
# 1

# 2          2
# 1 1
# 2

# 3          4
# f[2] + f[1] + f[0]
# 1 1 1 f[2]
# 2 1

# 1 2 f[1]
# 3 f[0]

# 4          7
# f[3]+ f[2]+f[1]
# 1+1+1+1 --- f[3]
# 1+2+1
# 2+1+1
# 3+1

# 1+1+2  --- f[2]
# 2+2

# 1+3    ---f[1]

# 5
# f[4]+ f[3] +f[2]
# 1+1+1+1 +1
# 1+1+2   +1
# 1+2+1   +1
# 2+1+1   +1
# 2+2     +1
# 1+3     +1
# 3+1     +1

# 1 2 2
# 2 1 2
# 3 2

# 1 1 3
# 2 3

def dp(a):
    if arr[a]:
        return arr[a]
    else:
        arr[a] = dp(a - 3) + dp(a - 2) + dp(a - 1)
        return arr[a]


arr = [1, 1, 2, 4, 7] + [0] * 11
for tc in range(int(input())):
    a = int(input())
    dp(a)
    print(arr[a])
