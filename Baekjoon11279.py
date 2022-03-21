import sys

sys.stdin = open("Baekjoon11279.txt")


def heap_sort():
    n = len(arr)
    for i in range(n):
        c = i
        while c:
            r = (c - 1) // 2
            if arr[r] < arr[c]:
                arr[c], arr[r] = arr[r], arr[c]
            c = r
    arr[0], arr[-1] = arr[-1], arr[0]
    return


N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    t = int(sys.stdin.readline())
    if t:
        arr.append(t)
    else:
        if arr:
            heap_sort()
            print(arr.pop())
        else:
            print(0)
