import sys

sys.stdin = open("ExpertAcademy4408.txt")
T = int(input())
for tc in range(1, T + 1):
    answer = 0
    N = int(input())
    arr = [0] * N
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    visited = [0] * N
    cnt = 0

    while 0 in visited:
        start = visited.index(0)  # 방문 안한곳을 시작점으로 잡고
        visited[start] = 1  # 시작점은 방문했으니 1.
        for g in range(start + 1, N):  # 시작점부터 끝까지 방문점 비교
            print(start, g, arr[start], arr[g], cnt)
            if arr[start][0] < arr[g][0] and arr[start][1] < arr[g][1] and arr[start][1] < arr[g][0] and visited[
                g] == 0:  # 시작점과 비교점의 출발점, 도착점, 도착점 출발점, (=경로가 겹치는지 )방문여부 각각 비교
                start = g  # 조건에 부합하면 시작점을 g로 잡아주고
                visited[g] = 1  # g를 시작점으로 함.
        cnt += 1
    answer = cnt
    print("#{} {}".format(tc, answer))

    # 꼭 윗라인 아랫라인 구분을 해줘야 하는가?
    # 어디서 오류가 생겼는가? ㅜㅜ
