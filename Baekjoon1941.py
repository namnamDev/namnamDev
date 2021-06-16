import sys

sys.stdin = open("Baekjoon1941.txt")

diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]


def dfs(now, strings, depth):
    if depth == 7 and strings.count('S') >= 4:
        tempVi = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for g in range(5):
                tempVi[i][g] = vi[i][g]
        for i in tempVi:
            print(i)
        global arr
        print()
        if tempVi not in arr:
            global an
            an += 1
            arr.append(tempVi)
        return
    for i in range(4):
        wy = now[0] + diry[i]
        wx = now[1] + dirx[i]
        if 0 <= wy < 5 and 0 <= wx < 5 and not vi[wy][wx]:
            adds = strings + board[wy][wx]
            if len(adds) >= 4:
                if adds.count('S') < len(adds) - 3:
                    return
            vi[wy][wx] = 1
            dfs([wy, wx], adds, depth + 1)
            vi[wy][wx] = 0
    return


board = [list(input()) for _ in range(5)]

an = 0
arr = []
for i in range(5):
    for g in range(5):
        vi = [[0] * 5 for _ in range(5)]
        dfs([i, g], '', 0)
for i in arr:
    print(i)
print(an)
