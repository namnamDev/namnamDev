import sys

sys.stdin = open("Baekjoon1181.txt")
T = int(input())
li = [input() for i in range(T)]
arr = [0] * 50
# li = list(set(li))
lenLi = len(li)
print(li)
for i in range(lenLi):
    for g in range(i + 1, lenLi):
        if li[i] == li[g]:
            li.pop(g)
            
        if len(li[i]) > len(li[g]):
            li[i], li[g] = li[g], li[i]
    print(li[i])
    arr[len(li[i])] += 1
print(arr)
for ii in li:
    print(ii)
