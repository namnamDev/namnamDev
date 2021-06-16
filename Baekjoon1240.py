import sys

sys.stdin = open("Baekjoon1240.txt")
N, M = map(int, input().split())
tree = [[0, 0, 0] for _ in range(N + 1)]
