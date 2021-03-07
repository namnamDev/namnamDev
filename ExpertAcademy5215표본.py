import sys

sys.stdin = open("ExpertAcademy5215.txt")


def powerset(idx):
    global score

    tmp_kcal = 0
    for i in range(n):
        if sel[i]:
            tmp_kcal += ingrd[i][1]
            if tmp_kcal > l:
                return

    if idx == n:
        tmp_score = 0
        for i in range(n):
            if sel[i]:
                tmp_score += ingrd[i][0]
                if score < tmp_score:
                    score = tmp_score

        return

    # idx 자리의 원소를 뽑고 간다.
    sel[idx] = 1
    powerset(idx + 1)
    # idx 자리의 원소를 안뽑고 간다.
    sel[idx] = 0
    powerset(idx + 1)


for t in range(1, int(input()) + 1):
    n, l = map(int, input().split())

    # [(점수, 칼로리), ...]
    ingrd = [tuple(map(int, input().split())) for _ in range(n)]

    # 부분집합 리스트
    sel = [0] * n

    # 점수 저장을 위한 변수
    score = 0

    powerset(0)

    print('#{} {}'.format(t, score))
