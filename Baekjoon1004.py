import sys
from pprint import pprint
sys.stdin = open("Baekjoon1004.txt")
T = int(input())
for tc in range(1,T+1):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    li = [0]*N
    for i in range(N):
        li[i] = list(map(int, input().split()))
