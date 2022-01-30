import sys

sys.stdin = open("Baekjoon2702.txt")

for tc in range(int(input())):
    A, B = map(int, input().split())
    a, b = A, B
    minP = 1
    an1 = 1
    while minP <= min(a, b):
        if not a % minP and not b % minP:
            a //= minP
            b //= minP
            an1 *= minP
            minP = 1
        minP += 1
    print(A * B // an1, an1)
