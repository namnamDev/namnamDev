import sys

sys.stdin = open("Baekjoon1593.txt")


def powerSet(Mnums, Nnums, str):
    global cnt
    if len(str) == N:
        cnt += 1
        return

    if Mnums == M:
        return

    if ord(Mw[Mnums]) > 90:
        Mw[Mnums] = chr(ord(Mw[Mnums]) - 32)
    if ord(Nw[Nnums]) > 90:
        Nw[Nnums] = chr(ord(Nw[Nnums]) - 32)

    if Mw[Mnums] == Nw[Nnums]:
        powerSet(Mnums + 1, Nnums + 1, str + Mw[Mnums])
    powerSet(Mnums + 1, Nnums, str)


N, M = map(int, input().split())
Nw, Mw = list(input()), list(input())
cnt = 0
powerSet(0, 0, "")
print(cnt)
