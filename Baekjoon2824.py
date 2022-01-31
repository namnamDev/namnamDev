import sys

sys.stdin = open("Baekjoon2824.txt")
N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))
nn = 1
mm = 1
for i in n:
    nn *= i
for i in m:
    mm *= i
print(nn, mm)
an = 1
