import sys

sys.stdin = open("Baekjoon1181.txt")
T = int(input())
li = [input() for i in range(T)]
arr = []
li = list(set(li))
lenLi = len(li)
for i in range(lenLi):
    for g in range(i + 1, lenLi):
        if len(li[i]) > len(li[g]):
            li[i], li[g] = li[g], li[i]
        elif len(li[i]) == len(li[g]):
            for f in range(len(li[i])):
                if ord(li[i][f]) < ord(li[g][f]):
                    li[i], li[g] = li[g], li[i]
for ii in li:
    print(ii)
