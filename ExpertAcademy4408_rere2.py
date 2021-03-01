import sys

sys.stdin = open("ExpertAcademy4408.txt")
for t in range(1, int(input()) + 1):
    visited = [0] * 201
    for _ in range(int(input())):
        start, end = map(int, input().split())
        if start > end:
            start, end = end, start
        start = (start + 1) // 2
        end = (end + 1) // 2
        for i in range(start, end + 1):
            visited[i] += 1
    print('#{} {}'.format(t, max(visited)))

    # 꼭 윗라인 아랫라인 구분을 해줘야 하는가?
    # 어디서 오류가 생겼는가? ㅜㅜ
