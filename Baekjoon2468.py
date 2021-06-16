import sys

sys.stdin = open('Baekjoon2468.txt')
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
for i in board:
    print(i)
