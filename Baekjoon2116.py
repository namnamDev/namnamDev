import sys

sys.stdin = open("Baekjoon2116.txt")

# def randomDice(nums):
#     global visited
#     if nums == T:
#         return
#     else:

dice = [5, 3, 4, 1, 2, 0]
T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]
print(arr)
maxs = 0
for g in range(6):
    visited = [[0] * 6 for _ in range(T)]
    cnt = 1
    downIdx = g
    upIdx = dice[downIdx]
    visited[0][downIdx] = 1
    visited[0][upIdx] = 1
    down = arr[0][downIdx]
    up = arr[0][upIdx]
    tempMaxs = 0
    for i in range(6):
        if visited[0][i] == 0:
            if tempMaxs < arr[0][i]:
                tempMaxs = arr[0][i]
    # print(down, up)
    # print(tempMaxs, g)
    while cnt < len(arr):
        tempArr = arr[cnt]
        tempVist = visited[cnt]
        downIdx = tempArr.index(up)
        upIdx = dice[downIdx]
        tempVist[downIdx] = 1
        tempVist[upIdx] = 1
        down = tempArr[downIdx]
        up = tempArr[upIdx]
        temp = 0
        for i in range(6):
            if tempVist[i] == 0:
                if temp < tempArr[i]:
                    temp = tempArr[i]
        # print(temp)
        tempMaxs += temp
        cnt += 1
        # print(down, up)
    #
    # print(tempMaxs)
    # for i in visited:
    #     print(i)
    if maxs < tempMaxs:
        maxs = tempMaxs
    # print(tempMaxs)

print(maxs)
