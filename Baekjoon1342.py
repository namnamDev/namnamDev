import sys

sys.stdin = open('Baekjoon1342.txt')


def back(paArr, befores):
    if len(paArr) == len(N):
        global cnt
        cnt += 1
        return
    for i in range(len(N)):
        if N[i] != befores and not vi[i] and not memo.get(paArr + N[i]):
            memo[paArr + N[i]] = 1
            vi[i] = 1
            back(paArr + N[i], N[i])
            vi[i] = 0


N = list(input())
cnt = 0
memo = {}
for ii in range(len(N)):
    vi = [0] * len(N)
    vi[ii] = 1
    back(N[ii], N[ii])
print(cnt)
