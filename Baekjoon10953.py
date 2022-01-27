import sys

sys.stdin = open('Baekjoon10953.txt')
for i in range(int(input())):
    print(sum(list(map(int, input().split(",")))))
