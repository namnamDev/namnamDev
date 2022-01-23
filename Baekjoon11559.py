import sys

sys.stdin = open("Baekjoon11559.txt")

from collections import deque

Y, X, popLeast = 12, 6, 4
board = [list(input()) for _ in range(Y)]
diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]
totalCnt = 0
# 터트릴 리스트 착출
while True:
    vi = [[0] * X for _ in range(Y)]
    pList = deque([])
    for y in range(Y):
        for x in range(X):
            if board[y][x] != "." and not vi[y][x]:
                tw = board[y][x]
                tQ = [[y, x]]
                vi[y][x] = 1
                Q = deque([[y, x]])
                while Q:
                    now = Q.popleft()
                    for ds in range(4):
                        wy = now[0] + diry[ds]
                        wx = now[1] + dirx[ds]
                        if 0 <= wy < Y and 0 <= wx < X and tw == board[wy][wx] and not vi[wy][wx]:
                            tQ.append([wy, wx])
                            Q.append([wy, wx])
                            vi[wy][wx] = 1
                if len(tQ) >= popLeast:
                    pList.append(tQ)
    if not len(pList):
        break
    totalCnt += 1
    # 터트리기
    while pList:
        tempList = pList.popleft()
        while tempList:
            now = tempList.pop()
            board[now[0]][now[1]] = "."

    # 빈 라인이 있는 줄 체크
    noLine = []
    for y in range(Y - 1):
        for x in range(X - 1):
            if x not in noLine and board[y][x] != "." and board[y + 1][x] == ".":
                noLine.append(x)
    # 줄 내리기
    print(noLine)
    while noLine:
        nowX = noLine.pop()
        cnt = 0
        for y in range(Y):
            if board[y][nowX] != ".":
                cnt += 1
        for ccnt in range(cnt):
            for y in range(Y - 1):
                if board[y][nowX] != "." and board[y + 1][nowX] == ".":
                    board[y + 1][nowX] = board[y][nowX]
                    board[y][nowX] = "."
print(totalCnt)
