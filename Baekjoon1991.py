import sys

sys.stdin = open("Baekjoon1991.txt")

# def pre():


T = int(input())
arr = [[0] * 3 for _ in range(T + 1)]
for i in range(T):
    M, L, R = input().split()
    # print(M, L, R)
    if L == ".":
        L = "@"
    if R == ".":
        R = "@"
    mother = ord(M) - 64
    left = ord(L) - 64
    right = ord(R) - 64
    arr[mother][1] = left
    arr[mother][2] = right
    if left:
        arr[left][0] = mother
    if right:
        arr[right][0] = mother
        # arr[ord(M) - 64][1] = ord(L) - 64
    # arr[ord(M) - 64][2] = ord(R) - 64
    # arr[ord(L) - 64][0] = ord(M) - 64
    # arr[ord(R) - 64][0] = ord(M) - 64
    # print(arr[mother])
for i in arr:
    print(i)
print(ord("A"), ord("Z"), chr(64), ord("G") - 64)
