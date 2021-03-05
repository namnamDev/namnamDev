import sys

sys.stdin = open("Baekjoon2313.txt")
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(N, arr)
    sums = 30 * 5 + 70 * 4 + 10 * 2 - 30
    print(sums)
