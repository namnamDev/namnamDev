import sys

sys.stdin = open("Baekjoon2171.txt")
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
arr.sort()

cnt = 0
for ii in range(N):
    now = arr[ii]

    x = now[0]
    y = now[1]
    xline = []
    yline = []
    for i in range(N):
        if arr[i][0] == x and arr[i][1] > y:
            xline.append(arr[i][1])
        if arr[i][1] == y and arr[i][0] > x:
            yline.append(arr[i][0])

    for i in xline:
        for g in yline:
            if [g, i] in arr:
                cnt += 1

print(cnt)
# for i in arr:
#     print(i)
