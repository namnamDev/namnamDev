import sys

sys.stdin = open('머지소트_병합정렬.txt')
arr = list(map(int, input().split()))


def bubble_sort(arr):
    n = len(arr)
    print(arr)
    for k in range(n - 1, -1, -1):
        for f in range(k):
            if arr[f] > arr[f + 1]:
                arr[f], arr[f + 1] = arr[f + 1], arr[f]


def selection_sort(arr):
    n = len(arr)
    for f in range(n - 1):  # 마지막 숫자는 자동으로 정렬되기 때문에 (숫자 개수-1) 만큼 반복한다.
        min_idx = f
        for s in range(f + 1, n):
            if arr[s] < arr[min_idx]:
                min_idx = s
        if min_idx != f:  # 최솟값이 자신이면 이동하지않음
            arr[f], arr[min_idx] = arr[min_idx], arr[f]


print(arr)
selection_sort(arr)
print(arr)
