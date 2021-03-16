import sys

from collections import deque

sys.stdin = open("ExpertAcademy10966.txt")

diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]

for tc in range(int(input())):
    N, M = map(int, input().split())  #
    visited = [[0] * M for _ in range(N)]  # 0으로 시작하면 모든 칸의 값이 +1된상태로 저장되므로  추후에 일괄 감산 예정
    board = []  # 0으로 시작하면 모든 칸의 값이 +1된상태로 저장되므로  추후에 일괄 감산 예정

    Q = deque()  # Queue로 풀 예정
    for y in range(N):
        temp = list(input())
        for x in range(M):
            if temp[x] == "W":
                visited[y][x] = 1
                Q.append([y, x])  # 물의 위치를 Q에 담아둠

    while len(Q):
        now = Q.popleft()
        for i in range(4):
            wy = now[0] + diry[i]  # 세로좌표
            wx = now[1] + dirx[i]  # 가로좌표
            if 0 <= wy < N and 0 <= wx < M:
                if visited[wy][wx] == 0:
                    visited[wy][wx] = visited[now[0]][now[1]] + 1
                    Q.append([wy, wx])

    ans = 0
    for i in visited:  # 결과값을 구하는 for문
        ans += sum(i)
    ans -= N * M  # 1씩 모두 초과되었으므로 감산.

    print("#{} {}".format(tc + 1, ans))
