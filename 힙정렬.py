array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]


# 1. 상향식: 특정 노드를 기준으로 위로 올라감
def heap_sort(array):
    n = len(array)
    # heap 구성
    for i in range(n):
        c = i
        while c != 0:
            r = (c - 1) // 2
            if array[r] < array[c]:
                array[r], array[c] = array[c], array[r]
            c = r
            print(array, "heapify")
    # 크기를 줄여가면서 heap 구성
    for j in range(n - 1, -1, -1):
        array[0], array[j] = array[j], array[0]
        r = 0
        c = 1
        while c < j:
            c = 2 * r + 1
            # 자식 중 더 큰 값 찾기
            if (c < j - 1) and (array[c] < array[c + 1]):
                c += 1
            # 루트보다 자식이 크다면 교환
            if (c < j) and (array[r] < array[c]):
                array[r], array[c] = array[c], array[r]
            r = c
            print(array)
    print(array)


heap_sort(array)
# 1, 10, 5, 8, 7, 6, 4, 3, 2, 9
#          1
#       10       5
#    8     7    6  4
#  3  2   9

#          10
#       1       5
#    8     7    6  4
#  3  2   9

#          10
#       8         5
#    1     7    6  4
#  3  2   9

#          10
#       8         6
#    1     7    5   4
#  3  2   9


#       10
#     9       6
#  3    8    5  4
# 1 2  7


#       7
#     9       6
#  3    8    5  4
# 1 2  10

#       9
#     7       6
#  3    8    5  4
# 1 2  10
