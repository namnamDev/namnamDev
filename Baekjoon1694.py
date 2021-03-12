import sys

sys.stdin = open("Baekjoon1694.txt")
for tc in range(2):
    arr = list(input().split('/'))
    board = [[0] * 8 for _ in range(8)]
    print(arr)
    for i in arr:
