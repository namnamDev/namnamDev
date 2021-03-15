import sys

sys.stdin = open("ExpertAcademy10966.txt")
for tc in range(int(input())):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    print(board)
