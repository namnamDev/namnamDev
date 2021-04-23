import sys
from collections import deque

sys.stdin = open('ExpertAcademy11780.txt')


def find(num):
    temp = board[num]
    for i in range(N):
        if temp[i]:
            if union[i] == i:
                union[i] = union[num]
            union[i] = union[num]
            if not vi[i]:
                vi[i] = 1
                find(i)


for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    board = [[0] * N for _ in range(N)]
    union = [0] * N
    for i in range(M):
        fir = arr[i * 2] - 1
        sec = arr[i * 2 + 1] - 1
        board[fir][sec] = 1
        board[sec][fir] = 1
    for i in range(N):
        union[i] = i
    vi = [0] * N
    print(union)
    for i in range(N):
        if not vi[i]:
            vi[i] = 1
            find(i)
    print(union)
    an = len(set(union))
    print("#{} {}".format(tc + 1, an))
    # Q = deque([arr[0], [arr[1]]])
