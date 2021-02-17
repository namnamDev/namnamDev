import sys
sys.stdin = open("ExpertAcademy1873.txt")

headDir = ['>', '<', 'v', '^']
dirx = [1, -1, 0, 0]
diry = [0, 0, 1, -1]
moveCmd = ['R', 'L', 'D', 'U']


def whereTank(li, H, W):
    for defh in range(H):
        for defw in range(W):
            a = li[defh][defw]
            if a in headDir:
                return [defh, defw, li[defh][defw]]


def shoot(board, start, H, W):
    temp = 0
    for head in range(4):
        if start[2] == headDir[head]:
            temp = head
            print("S", temp, headDir[temp])
            print(start[0] + diry[temp], start[1] + dirx[temp])
            break
    shooty = start[0]
    shootx = start[1]
    while 0 <= shooty+diry[temp] < H and 0 <= shootx+dirx[temp] < W:
        if board[shooty+diry[temp]][shootx+dirx[temp]] == "*":
            shooty += diry[temp]
            shootx += dirx[temp]
            board[shooty][shootx] = '.'
            break
        elif board[shooty+diry[temp]][shootx+dirx[temp]] == "#":
            break
        else:
            shooty += diry[temp]
            shootx += dirx[temp]
    return board


def move(board, start, H, W, cmd):
    temp = 0
    for cmdh in range(4):
        if cmd == moveCmd[cmdh]:
            temp = cmdh
            print(cmd, temp)
            print(start[0] + diry[temp], start[1] + dirx[temp])
            break
    if 0 <= start[0]+diry[temp] < H and 0 <= start[1]+dirx[temp] < W:
        if board[start[0]+diry[temp]][start[1]+dirx[temp]] == ".":
            board[start[0]][start[1]] = "."
            start[0] += diry[temp]
            start[1] += dirx[temp]
    start[2] = headDir[temp]
    board[start[0]][start[1]] = start[2]
    return board


T = int(input())
for tc in range(1,T+1):
    H, W = map(int,input().split())
    board = [0]*H
    for h in range(H):
        board[h] = list(input())
    start = whereTank(board, H, W)

    N = int(input())
    cmd = list(input())
    for command in cmd:
        if command == 'S':
            board = shoot(board, start, H, W)
            print("---")
            for i in board:
                print(*i)
        else:
            board = move(board, start, H, W, command)
            print("---")
            for i in board:
                print(*i)

    ans = ""
    for ff in board[0]:
        ans += ff
    print('#{} {} '.format(tc, ans))

    for f in range(1, H):
        ans = ""
        for fff in board[f]:
            ans += fff
        print(ans)
