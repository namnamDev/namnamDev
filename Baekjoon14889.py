import sys

sys.stdin = open("Baekjoon14889.txt")


def cal(pa_str):
    if not used.get(pa_str):
        aa_li = list(map(int, pa_str.split(",")))
        aa_size = len(aa_li)
        val = 0
        for i in range(aa_size):
            for f in range(i + 1, aa_size):
                val += board[aa_li[i] - 1][aa_li[f] - 1] + board[aa_li[f] - 1][aa_li[i] - 1]
        used[pa_str] = val
    return used[pa_str]


def lec(paArr, idx):
    if len(paArr) == N // 2:
        # print(paArr, vi)
        aa = ""
        for i in range(1, N + 1):
            if not vi[i]:
                aa += "," + str(i)
        bb = ",".join(map(str, paArr))
        a_val = cal(aa[1::])
        b_val = cal(bb)
        an_list.append(abs(a_val - b_val))
        return

    for i in range(idx, N + 1):
        vi[i] = 1
        lec(paArr + [i], i + 1)
        vi[i] = 0


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
used = {}
vi = [0] * (N + 1)
an_list = []
lec([], 1)
print(min(an_list))
