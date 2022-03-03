import sys

sys.stdin = open("Baekjoon16953.txt")


def backs(paN, cnt):
    global min_cnt
    if cnt >= min_cnt or paN > B:
        return
    if paN == B:
        min_cnt = cnt
        return
    backs(paN * 2, cnt + 1)
    backs(int(str(paN) + "1"), cnt + 1)


A, B = map(int, input().split())
min_cnt = 10 ** 9
backs(A, 1)
if min_cnt == 10 ** 9:
    min_cnt = -1
print(min_cnt)
