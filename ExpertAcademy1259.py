import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy1259.txt")

def powerset(temp):
    for i in range(N):
        if arr[i][0] == temp[1] and

for tc in range(int(input())):
    print(tc)
    N = int(input())
    lines = list(map(int, input().split()))
    arr = [0] * N
    used = [0]*N
    for i in range(0, N * 2, 2):
        arr[i // 2] = [lines[i], lines[i + 1]]
    an = []
    for i in arr:
        print(i)

