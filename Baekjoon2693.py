import sys

sys.stdin = open("Baekjoon2693.txt")
for _ in range(int(input())):
    print(sorted(list(map(int, input().split())))[-3])
