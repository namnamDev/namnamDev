import sys

sys.stdin = open("Baekjoon1991.txt")


def preorder(num):
    global pre_order
    if num:
        temp = arr[num]
        pre_order += temp[0]
        preorder(temp[1])
        preorder(temp[2])


def inorder(num):
    global in_order
    if num:
        temp = arr[num]
        inorder(temp[1])
        in_order += temp[0]
        inorder(temp[2])


def postorder(num):
    global post_order
    if num:
        temp = arr[num]
        postorder(temp[1])
        postorder(temp[2])
        post_order += temp[0]


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
    arr[mother][0] = M
    arr[mother][1] = left
    arr[mother][2] = right
pre_order = ''
in_order = ''
post_order = ''

preorder(1)
inorder(1)
postorder(1)
print(pre_order)
print(in_order)
print(post_order)
