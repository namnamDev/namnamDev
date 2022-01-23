import sys

sys.stdin = open('Baekjoon10546.txt')
N = int(input())
arr1 = [""] * N
arr2 = [""] * (N - 1)
for i in range(N):
    arr1[i] = input()
for g in range(N - 1):
    arr2[g] = input()
arr1.sort()
arr2.sort()
an = ""
for ii in range(N - 1):
    if arr1[ii] != arr2[ii]:
        an = arr1[ii]
        break
if an == "":
    an = arr1[-1]
print(an)
