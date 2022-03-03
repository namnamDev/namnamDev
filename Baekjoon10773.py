import sys

sys.stdin = open("Baekjoon10773.txt")
N = int(input())
arr = []
for i in range(N):
    a = int(input())
    if a:
        arr.append(a)
    else:
        arr.pop()
print(sum(arr))
