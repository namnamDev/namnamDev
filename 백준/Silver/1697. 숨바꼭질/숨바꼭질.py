from collections import deque

N, M = map(int, input().split())
board = [0] * 200002
Q = deque([N])
board[N] = 1
while len(Q):
    t = Q.popleft()
    if board[M]:
        break
    if 0 <= t * 2 < 200002 and not board[t * 2]:
        board[t * 2] = board[t] + 1
        Q.append(t * 2)
    if 0 <= t - 1 and not board[t - 1]:
        board[t - 1] = board[t] + 1
        Q.append(t - 1)
    if t + 1 < 200002 and not board[t + 1]:
        board[t + 1] = board[t] + 1
        Q.append(t + 1)
        
print(board[M] - 1)