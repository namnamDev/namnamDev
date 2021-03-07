import sys

sys.stdin = open("Baekjoon1991.txt")


def pre():



T = int(input())
arr = [0] * (T + 1)
for tc in range(T):
    M, L, R = input().split()
    if L == ".":
        L = "@"
    if R == ".":
        R = "@"
    arr[ord(M) - 64] = [ord(L) - 64, ord(R) - 64]
print(arr)
print(ord("A"), ord("Z"), chr(64))
