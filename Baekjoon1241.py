import sys

sys.stdin = open('Baekjoon1241.txt')

N = int(input())
arr = [int(input()) for _ in range(N)]
for i in range(N):
    idx = i
    student = arr[idx]
    cnt = 0
    an = 0
    temp1 = arr[:idx]
    temp2 = arr[idx:]
    for g in temp1:
        if not student % g:
            an += 1
    for g in temp2:
        if not student % g:
            an += 1
    # while cnt < N:
    #     idx = idx % N
    #     if not student % arr[idx]:
    #         an += 1
    #     idx += 1
    #     cnt += 1
    print(an - 1)
