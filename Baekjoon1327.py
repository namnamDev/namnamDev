import sys

sys.stdin = open("Baekjoon1327.txt")
N, K = map(int, input().split())
li = list(map(int, input().split()))
print(N, K, li)
