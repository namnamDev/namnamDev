import sys

sys.stdin = open('Baekjoon1032.txt')
N = int(input())
answer = list(input())
for i in range(N - 1):
    temp = input()
    for g in range(len(answer)):
        if answer[g] != "?" and answer[g] != temp[g]:
            answer[g] = "?"
a = ""
for ii in answer:
    a += ii
print(a)
