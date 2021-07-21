import sys

sys.stdin = open("Baekjoon1181.txt")
T = int(input())
counting = [[] for _ in range(51)]
an = ""
for i in range(T):
    w = input()
    counting[len(w)].append(w)
for i in range(51):
    if counting[i]:
        counting[i] = list(set(counting[i]))
        # print(counting[i])
        counting[i].sort()
        for g in counting[i]:
            an += g + '\n'

print(an)

# li = [input() for i in range(T)]
# arr = []
# li = list(set(li))
# print(li)
