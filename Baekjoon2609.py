import sys

sys.stdin = open('Baekjoon1920.txt')


def bin(start, end, bIdx):
    # print(start, end, bIdx)
    if start > end:
        return
    else:
        mid = (start + end) // 2
        if A[mid] > B[bIdx]:
            bin(start, mid - 1, bIdx)
        elif A[mid] < B[bIdx]:
            bin(mid + 1, end, bIdx)
        else:
            vi[bIdx] = 1
            return


N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))
vi = [0] * M
for i in range(M):
    bin(0, N - 1, i)
for i in vi:
    print(i)
