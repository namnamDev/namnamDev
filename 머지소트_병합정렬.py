import sys

sys.stdin = open('머지소트_병합정렬.txt')
arr = list(map(int, input().split()))


def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        print(low, mid, high)
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1
        for ll in range(l, mid):
            temp.append(arr[ll])
        for hh in range(h, high):
            temp.append(arr[hh])
        print(temp)
        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))


print(arr)
merge_sort(arr)
print(arr)
