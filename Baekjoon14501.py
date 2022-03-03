import sys

sys.stdin = open("Baekjoon14501.txt")
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * N
