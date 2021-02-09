import sys
sys.stdin = open("ExpertAcademy1208.txt")

#
# def my_max(arr):
#     ans = 0
#     for g in arr:
#         if ans < g:
#             ans = g
#     return ans


def my_mix(arr):
    ans_min, ans_max = arr[0], 0
    for j in arr:
        if ans_min > j:
            ans_min = j
        elif ans_max < j:
            ans_max = j
    return ans_max, ans_min


for i in range(1, 11):
    dump = int(input())
    li = list(map(int, input().split()))
    for h in range(dump):
        temp_max, temp_min = my_mix(li)
    print(temp_max, temp_min)


