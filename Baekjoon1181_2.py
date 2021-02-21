import sys

sys.stdin = open("Baekjoon1181.txt")
T = int(input())
li = [input() for i in range(T)]
count = [] * 50
arr = []
lenLi = len(li)
i = 0
while i < T:
    for g in range(i + 1, T):
        if len(li[i]) > len(li[g]):
            li[i], li[g] = li[g], li[i]
        # if li[i] == li[g]:
        #     li.pop(i)
        #     i += 1
    i += 1
for ii in li:
    print(ii)
