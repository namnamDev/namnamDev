from collections import deque

N = int(input())
tree = [[] for _ in range(N + 1)]
needTree = [[] for _ in range(N + 1)]
disagree = [0] * (N + 1)
timeList = [0] * (N + 1)
visit = [0] * (N + 1)
for i in range(1, N + 1):
    tarr = list(map(int, input().split()))
    timeList[i] = tarr[0]
    for idx in range(1, len(tarr) - 1):
        tree[tarr[idx]].append(i)
        needTree[i].append(tarr[idx])
        disagree[i] += 1
Q = deque([])
for i in range(1, N + 1):
    if not disagree[i]:
        Q.append(i)
        visit[i] += timeList[i]
while Q:
    now = Q.popleft()
    for e in tree[now]:
        disagree[e] -= 1
        if not disagree[e] and not visit[e]:
            Q.append(e)
            tempNeed = 0
            for need in needTree[e]:
                tempNeed = max(visit[need], tempNeed)
            visit[e] = timeList[e] + tempNeed
for i in range(1, N + 1):
    print(visit[i])