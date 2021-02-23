import sys

sys.stdin = open("ExpertAcademy1219.txt")


def travel(N):
    if arrDict.get(N):
        templi = arrDict.get(N)
        for i in templi:
            if visited[99]:
                break
            if visited[i] == 0:
                visited[i] = 1
                travel(i)


SIZE = 100
for tc in range(1, 11):
    arrDict = {}
    visited = [0] * 100
    t, n = map(int, input().split())
    li = list(map(int, input().split()))
    for i in range(0, len(li), 2):
        li[i], li[i + 1]
        arrDict[li[i]] = arrDict.get(li[i], []) + [li[i + 1]]
    an = 0
    travel(0)
    if visited[99] == 1:
        an = 1
    print("#{} {}".format(t, an))
