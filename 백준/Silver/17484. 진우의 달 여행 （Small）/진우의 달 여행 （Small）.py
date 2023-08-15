import sys
input = sys.stdin.readline


def my_lec(depth, pre_dir, now_idx, pre_value):
    if depth >= N:
        answer.append(pre_value)
        return

    if visit[depth][now_idx]:
        return

    visit[depth][now_idx] = pre_value + arr[depth][now_idx]

    for d in dr:
        w = now_idx + d
        if d != pre_dir and 0 <= w < M:
            my_lec(depth + 1, d, w, visit[depth][now_idx])

    visit[depth][now_idx] = 0


dr = [-1, 0, 1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
answer = []
for i in range(M):
    my_lec(0, -2, i, 0)
print(min(answer))