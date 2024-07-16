import sys

sys.stdin = open("Baekjoon11478.txt")

S = input()
arr = []
for i in range(len(S)):
    for f in range(i + 1, len(S)+1):
        arr.append(S[i:f])
print(len(set(arr)))