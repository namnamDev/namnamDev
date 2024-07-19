import sys

sys.stdin = open("Baekjoon2960.txt")


def my_def(N, K):
    count = 0
    for i in range(2, N + 1):
        if not arr[i]:
            t = i
            while t < N + 1:
                if not arr[t]:
                    arr[t] = 1
                    count += 1
                    if count == K:
                        return t
                t += i

N, K = map(int, input().split())
arr = [0] * (N+1)
arr[0] = 1
arr[1] = 1
an = my_def(N, K)
print(an)