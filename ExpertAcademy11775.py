import sys

sys.stdin = open('ExpertAcademy11775.txt')


def powerset(idx, val):
    global an
    if val >= an:
        return
    if 0 not in vi:
        an = min(an, val)
    for i in range(N):
        if not vi[i]:
            vi[i] = 1
            powerset(idx + 1, val + table[idx][i])
            vi[i] = 0


for tc in range(int(input())):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    an = 99999999999999
    vi = [0] * N
    powerset(0, 0)
    print("#{} {}".format(tc + 1, an))
