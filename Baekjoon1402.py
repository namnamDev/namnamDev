import sys

sys.stdin = open("Baekjoon1402.txt")

for tc in range(int(input())):
    N, K = map(int, input().split())
    dpPlus = [0] * N
    dpMuli = [0] * N
