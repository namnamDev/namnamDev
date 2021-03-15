import sys

sys.stdin = open("ExpertAcademy4012.txt")

T = int(input())


def cal_score(arr):
    # 점수 계산
    score = 0
    for i in arr:
        for j in arr:
            # 행렬 대각선 원소 계산 제외
            if i == j:
                continue
            score += graph[i][j]
    return score


def solve(index, arr):
    global ans

    # 식재료 조합의 개수가 전체 개수의  1/2 이면
    if len(arr) == N // 2:
        # 기존 식재료 조합 점수 계산
        s1 = cal_score(arr)

        # 사용하지 않은 나머지 식재료 찾기
        arr2 = []
        for j in range(N):
            if j not in arr:
                arr2.append(j)

        # 나머지 식재료 점수 계산
        s2 = cal_score(arr2)

        # 점수 차이 계산
        score = abs(s1 - s2)

        # 최솟값 갱신
        if score < ans:
            ans = score
        return

    # 마지막 식재료 라면 종료
    if index == N:
        return
    else:
        # 현재 식재료 넣어서 다음 인덱스 호출
        solve(index + 1, arr + [index])

        # 현재 식재료 넣지않고 다음 인덱스 호출
        solve(index + 1, arr)


for t in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 최솟값
    ans = 10e9

    # 식재료 인덱스, 식재료 조합 리스트
    solve(0, [])

    print(f"#{t + 1} {ans}")
