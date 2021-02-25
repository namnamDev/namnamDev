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
        temp = visited.index(0)
        # print(temp)
        visited[temp] = 1
        for g in range(temp + 1, N):
            # print(temp, g, arr[temp], arr[g])
            # print(arr[temp][1] < arr[g][0])
            if arr[temp][0] < arr[g][0] and arr[temp][1] < arr[g][1] and arr[temp][1] < arr[g][0] and visited[g] == 0:
                # print(visited)
                temp = g
                visited[g] = 1
        cnt += 1
        # print(visited)
    # print(cnt)
    answer = cnt
    # print(visited)
    print("#{} {}".format(tc, answer))
