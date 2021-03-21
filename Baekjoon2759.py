import sys

sys.stdin = open("Baekjoon2759.txt")

for tc in range(int(input())):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    print(N, arr)
    temp = []
    idx = 0

    for i in range(N - 1):
        if arr[i] > arr[i + 1]:
            idx = i
            break
    # while arr[idx] > arr[idx + 1]:
    #     idx += 1

    temp = arr[:idx + 1]
    print(idx, temp)
    lenTemp = len(temp)
    for g in range(lenTemp // 2):
        arr[g], arr[lenTemp - g - 1] = arr[lenTemp - g - 1], arr[g]

    print(arr)

    # temp = []
    # for i in range(N - 1):
    #     if arr[i] > arr[i + 1]:
    #         temp.append(arr[i])
    #         print(temp)
    #     else:
    #         for g in range(N):
    #             print(arr)
    #             arr[g], arr[i - g] = arr[i - g], arr[g]
    #             print(arr, i, g)
    print(arr)
