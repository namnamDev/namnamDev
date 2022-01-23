import sys

sys.stdin = open("Baekjoon1268.txt")
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
vi = [[]] * N
for i in board:
    for stu in i
