import sys

sys.stdin = open('Baekjoon12101.txt')


def choi(paArr):
    if len(an) == m or sum(paArr) > n:
        return
    if sum(paArr) == n:
        an.append(paArr)
        return
    for i in range(1, 4):
        choi(paArr + [i])


n, m = map(int, input().split())
an = []
choi([])
if m > len(an):
    print(-1)
else:
    reAn = an[m - 1]
    re = str(reAn[0])
    for i in range(1, len(reAn)):
        re += "+" + str(reAn[i])

    print(re)
