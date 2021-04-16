import sys

sys.stdin = open('Baekjoon1759.txt')


def powerset(idx, arr_i):
    if idx == C:
        return
    if len(arr_i) == L:
        check = False
        for i in word:
            if i in arr_i:
                check = True
                break
        if check:
            print(arr_i)
    for i in range(idx + 1, C):
        powerset(i, arr_i + arr[i])


word = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
for i in range(C - L + 1):
    powerset(i, arr[i])
