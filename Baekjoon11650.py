import sys

sys.stdin = open('Baekjoon11650.txt')
N = int(input())
arr = [list(map(int, (input().split()))) for _ in range(N)]
arr.sort()
for i in arr:
    print(*i)
