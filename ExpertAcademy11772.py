import sys

sys.stdin = open('ExpertAcademy11772.txt')


def binary(num, start, end):
    mid = (start + end) // 2
    if start >= end:
        return
    if num > A[mid]:
        global right
        right += 1
        binary(num, mid + 1, end)
    elif num < A[mid]:
        global left
        left += 1
        binary(num, start, mid)
    else:
        global cnt
        cnt += 1


for tc in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    for i in B:
        left = right = 0
        binary(i, 0, N)

    print("#{} {}".format(tc + 1, cnt))
