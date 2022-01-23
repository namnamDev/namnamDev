import sys

sys.stdin = open("Baekjoon2022TestA.txt")
# def choice(paArr):

N, d = map(int, input().split())
N += 1
realAn = "-1"
an = ""
tempN = N
vi = [0] * d
while tempN >= d:
    vi[tempN % d] += 1
    an = str(tempN % d) + an
    tempN //= d
an = str(tempN) + an
vi[tempN] += 1
print(an)
print(vi)

print(realAn)
# 5를 3진법으로 12
# 5%3 = 2 5//3 = 1
