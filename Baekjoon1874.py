import sys

sys.stdin = open("Baekjoon1764.txt")
K, N = map(int, input().split())
an = {}
for i in range(K):
    t = input()
    an[t] = 1
ann = []
for g in range(N):
    s = input()
    if an.get(s):
        ann.append(s)
    else:
        an[s] = 1
print(len(ann))
ann.sort()
for i in ann:
    print(i)
