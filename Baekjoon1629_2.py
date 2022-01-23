import sys

A, B, C = map(int, input().split())
an = 1
arr = []
cnt = 0
for _ in range(B):
    an *= A
    temp = an % C
    temp2 = an // C
    if temp not in arr:
        arr.append(temp)
    else:
        break
    cnt += 1
    if temp2:
        an = temp
print(arr[B % len(arr)])
