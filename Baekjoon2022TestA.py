import sys

sys.stdin = open("Baekjoon2022TestA.txt")

N, d = map(int, input().split())
N += 1
realAn = "-1"
while N < 10 ** 9:
    an = ""
    tempN = N
    vi = [0] * d
    while tempN >= d:
        vi[tempN % d] += 1
        an = str(tempN % d) + an
        tempN //= d
    an = str(tempN) + an
    vi[tempN] += 1

    check = False
    for i in vi:
        if i != 1:
            check = True
            break
    if not check:
        print(an)
        realAn = N
        break

    if sum(vi) > d:
        break
    N += 1

print(realAn)
# 5를 3진법으로 12
# 5%3 = 2 5//3 = 1
