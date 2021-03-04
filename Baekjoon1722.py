def dfs1(dept):
    global visited
    global cnt
    global an
    if cnt == arr[0]:
        return

    if dept == N:
        cnt += 1
        an = temp
        # print(temp, cnt)
        return
    else:
        for i in range(1, N + 1):
            if visited[i] != 1:
                visited[i] = 1
                temp[dept] = i
                dfs1(dept + 1)
                visited[i] = 0


# def dfs2(N):


N = int(input())
arr = list(map(int, input().split()))
M = arr.pop(0)
cnt = 0
li = list(range(1, N + 1))
visited = [0] * (N + 1)
temp = [0] * N
an = []
if M == 1:
    dfs1(0)
    print(an)
else:
    dfs2(0)
