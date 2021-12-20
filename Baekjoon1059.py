import sys

sys.stdin = open('Baekjoon1059.txt')
L = int(input())
arr = list(map(int, input().split()))
N = int(input())
arr.sort()
