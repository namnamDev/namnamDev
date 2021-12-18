import sys

sys.stdin = open('Baekjoon1780.txt')


def bin(ystart, xstart, size):
    a = board[ystart][xstart]
    if size > 0:
        for i in range(ystart, ystart + 3 ** size):
            for g in range(xstart, xstart + 3 ** size):
                print(i, g, board[i][g], a, "++")
                if a != board[i][g]:
                    size -= 1
                    for ii in range(3):
                        for gg in range(3):
                            # print((3 ** size) * ii, (3 ** size) * gg, size, a)
                            bin((3 ** size) * ii, (3 ** size) * gg, size)
                    return
    else:
        print(ystart, xstart)
    print(a, "add 1")
    ss[a] += 1


T = int(input())
board = [list(map(int, input().split())) for _ in range(T)]
ss = [0, 0, 0]

bin(0, 0, 2)
print(ss)
