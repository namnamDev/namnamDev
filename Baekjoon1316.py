import sys

sys.stdin = open("Baekjoon1316.txt")
T = int(input())
cnt = 0
for i in range(T):
    n = input()
    arr = []
    for g in range(len(n)):
        if n[g] not in arr:
            arr += [n[g]]
            # print(arr)
        elif n[g] != arr[-1]:
            break
        if g == len(n) - 1:
            cnt += 1
print(cnt)
