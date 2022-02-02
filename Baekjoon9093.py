import sys

sys.stdin = open("Baekjoon9093.txt")
for _ in range(int(input())):
    a = list(input().split())
    an = ""
    for i in range(len(a)):
        an += a[i][::-1] + " "
    print(an)
