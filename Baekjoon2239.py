import sys
from pathlib import Path

sys.stdin = open(Path(__file__).stem + ".txt")


def ga(y, x):
    tA = board[y].copy()
    vi = [0] * 9
    for i in range(9):
        vi[tA[i] - 1] += 1
    tc = vi.count(0)

    if tc > 1 or tc == 0:
        return False
    elif tc == 1:
        board[y][x] = vi.index(0) + 1
        return True


def se(y, x):
    tA = []
    vi = [0] * 9
    for i in range(9):
        tA.append(board[i][x])
        vi[board[i][x]] += 1
    tc = vi.count(0)

    if tc > 1 or tc == 0:
        return False
    elif tc == 1:
        board[y][x] = vi.index(0) + 1
        return True


def sa(y, x):
    return


board = [list(map(int, input())) for _ in range(9)]
# for i in board:
#     print(i)
