import sys

sys.stdin = open("Baekjoon2615.txt")


def oh():
    for i in range(N):
        for g in range(N):
            bw = board[i][g]
            if bw != "0":
                y = i
                x = g
                for d in range(4):
                    cnt = 1
                    tempArr = [[x, y]]
                    while True:
                        wy = y + dry[d]
                        wx = x + drx[d]
                        if 0 <= wy < N and 0 <= wx < N and board[wy][wx] == bw:
                            tempArr.append([wx, wy])
                            y = wy
                            x = wx
                            cnt += 1
                        else:
                            break
                    y = i
                    x = g
                    while True:
                        wy = y - dry[d]
                        wx = x - drx[d]
                        if 0 <= wy < N and 0 <= wx < N and board[wy][wx] == bw:
                            tempArr.append([wx, wy])
                            y = wy
                            x = wx
                            cnt += 1
                        else:
                            break
                    if cnt == 5:
                        tempArr.sort()
                        an = bw
                        an2 = [tempArr[0][1] + 1, tempArr[0][0] + 1]
                        return [an, an2]


N = 19
dry = [0, 1, 1, 1]
drx = [1, 0, 1, -1]
board = [input().split() for _ in range(N)]

aa = oh()
if aa:
    print(aa[0])
    print(*aa[1])
else:
    print("0")
