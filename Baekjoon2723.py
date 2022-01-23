import sys

sys.stdin = open("Baekjoon2723.txt")


def choice(paArr, idx):
    global AN

    print(paArr)
    if idx == N:
        return
    for i in range(idx, N):
        if not vi[i]:
            AN += 1
            vi[i] = 1
            choice(paArr + [i], i + 1)
            vi[i] = 0


tc = int(input())

for t in range(tc):
    AN = 0
    N = int(input())
    # for i in range(N):
    vi = [0] * N
    choice([], 0)

    print(AN)
