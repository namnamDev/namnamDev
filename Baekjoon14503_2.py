import sys

sys.stdin = open('Baekjoon14503.txt')
N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(N, M)
print(r, c, d)
dry = [-1, 0, 1, 0]
drx = [0, 1, 0, -1]
for i in board:
    print(i)
run = True
answer = 0
while run:
    print(r, c, d)
    for i in board:
        print(i)
    if not board[r][c]:
        print('clean', d)
        answer += 1
        board[r][c] = 2  # 1번 현재위치 청소
    turns = 0
    ifnot = True
    for i in range(4):  # 왼쪽돌면서 써칭
        turns += 1  # 한번 돌았습니다
        d -= 1
        if d < 0:
            d = 3  # 빙글 돌기
        wy = r + dry[d]
        wx = c + drx[d]
        if 0 <= wy < N and 0 <= wx < M and not board[wy][wx]:  # 2-a만족시
            r = wy
            c = wx
            print(r, c, d)
            # print()
            ifnot = False
            break  # break으로 끊고 1번부터함
    # print('ifnot')
    if ifnot:  # 청소 못했을때
        wy = r - dry[d]  # 현재방향 유지 후진
        wx = c - drx[d]
        if 0 <= wy < N and 0 <= wx < M and board[wy][wx] == 2:
            r = wy
            c = wx
        else:
            run = False
print(answer)
