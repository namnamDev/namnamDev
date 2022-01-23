import sys

sys.stdin = open('Baekjoon15665.txt')


def choice(pArr):
    if len(pArr) == M:
        print(*pArr)
        return
    else:
        for i in range(lenArr):
            choice(pArr + [arr[i]])


N, M = map(int, input().split())
arr = list(set(list(map(int, input().split()))))
arr.sort()
lenArr = len(arr)
print(arr)
choice([])
