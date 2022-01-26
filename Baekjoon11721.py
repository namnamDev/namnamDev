import sys

sys.stdin = open("Baekjoon14940.txt")
s = input()
while s:
    print(s[:10])
    s = s[10:]
