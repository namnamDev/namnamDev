import sys

sys.stdin = open("ExpertAcademy4408.txt")
T = int(input())
for tc in range(1, T + 1):
    answer = 0
    N = int(input())
    arr = [0] * N
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    visited = [0] * 201
    cnt = 0
    for i in arr:
        a1, a2 = i[0], i[1]
        a1 //= 2
        a2 //= 2
        # if a1 % 2:
        #     a1 = a1 // 2 - 1
        # else:
        #     a1 //= 2
        # if a2 % 2:
        #     a2 = a2 // 2 - 1
        # else:
        #     a2 //= 2
        print(a1, a2)
        if a1 < a2:
            for g in range(a1, a2 + 1):
                # print(g, end=" ")
                visited[g] += 1
        else:
            for g in range(a1, a2 - 1, -1):
                # print(g, end=" ")
                visited[g] += 1
    # print(visited)
    print("#{} {}".format(tc, max(visited)))

    # 꼭 윗라인 아랫라인 구분을 해줘야 하는가?
    # 어디서 오류가 생겼는가? ㅜㅜ
