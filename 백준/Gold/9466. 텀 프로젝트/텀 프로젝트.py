from collections import deque

T = int(input())
for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (n + 1)
    indegree = [0] * (n + 1)
    for i in range(1, n + 1):
        tree[i] = arr[i - 1]
        indegree[arr[i - 1]] += 1
    Q = deque([])
    for i in range(1, n + 1):
        if not indegree[i]:
            Q.append(i)
    while Q:
        n = Q.popleft()
        w = tree[n]
        indegree[w] -= 1
        if not indegree[w]:
            Q.append(w)
    print(indegree.count(0) - 1)