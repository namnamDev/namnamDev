import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy1247.txt")


def powerset(arr, num, idx):
    global res
    if num > res:
        return
    if 0 not in visited:
        num += abs(company[0] - cust[arr[0]][0]) + abs(company[1] - cust[arr[0]][1])
        num += abs(home[0] - cust[idx][0]) + abs(home[1] - cust[idx][1])
        res = min(res, num)
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            val = abs(cust[i][0] - cust[idx][0]) + abs(cust[i][1] - cust[idx][1])
            powerset(arr + [i], num + val, i)
            visited[i] = 0


for tc in range(int(input())):
    N = int(input())
    line = list(map(int, input().split()))
    company = [line[0], line[1]]
    home = [line[2], line[3]]
    cust = []
    res = 999999999999999999999999
    for i in range(4, len(line), 2):
        cust.append([line[i], line[i + 1]])
    for i in range(N):
        visited = [0] * N
        powerset([], 0, i)
    print("#{} {}".format(tc + 1, res))
# 1 200
# 2 304
# 3 265
# 4 307
# 5 306
# 6 366
# 7 256
# 8 399
# 9 343
# 10 391
