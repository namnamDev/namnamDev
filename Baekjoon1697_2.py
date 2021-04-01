from collections import deque

N, M = map(int, input().split())
mins = abs(M - N)
board = [0] * 200000
Q = deque([[N, 0]])
while len(Q):
    temp = Q.popleft()
    n, cnt = temp[0], temp[1]
    diry = [2 * n, n - 1, n + 1]
    diry.sort()
    for i in diry:
        if cnt > mins:
            break
        if M == i:
            if mins > cnt:
                mins = cnt + 1
            break
        else:
            if i < 200000:
                if board[i] == 0:
                    Q.append([i, cnt + 1])
                    board[i] = 1
print(mins)
