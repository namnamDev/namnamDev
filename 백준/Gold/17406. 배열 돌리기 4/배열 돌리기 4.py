def myCopy():
    res = [[0] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            res[y][x] = originalMatrix[y][x]
    return res


def turn():
    matrix = myCopy()
    for i in range(K):
        ry, cx, s = arr[vi[i] - 1]
        ry -= 1
        cx -= 1
        for ss in range(1, s + 1):
            startX = cx - ss
            startY = ry - ss
            endX = cx + ss
            endY = ry + ss
            tempArr = []
            # topRow
            for tx in range(startX, endX):
                tempArr.append([startY, tx])
            # rightCol
            for ty in range(startY, endY):
                tempArr.append([ty, endX])
            # botRow
            for tx in range(endX, startX, -1):
                tempArr.append([endY, tx])
            # leftCol
            for ty in range(endY, startY, -1):
                tempArr.append([ty, startX])
            tempY, tempX = tempArr[-1]
            startVal = matrix[tempY][tempX]
            for idx in range(len(tempArr) - 1, 0, -1):
                beforeY, beforeX = tempArr[idx - 1]
                nowY, nowX = tempArr[idx]
                matrix[nowY][nowX] = matrix[beforeY][beforeX]
            matrix[tempArr[0][0]][tempArr[0][1]] = startVal
    # print(tempArr)
    # res = 100 * N * M
    global res
    for m in matrix:
        res = min(res, sum(m))
    return


def lec(pcnt):
    if pcnt == K + 1:
        turn()
        return
    for i in range(K):
        if not vi[i]:
            vi[i] = pcnt
            lec(pcnt + 1)
            vi[i] = 0


N, M, K = map(int, input().split())
originalMatrix = [list(map(int, input().split())) for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(K)]
vi = [0] * K
res = 100 * N * M
lec(1)
print(res)