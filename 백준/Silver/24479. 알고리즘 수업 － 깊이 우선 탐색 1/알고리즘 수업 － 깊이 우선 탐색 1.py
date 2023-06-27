N, M, R = map(int, input().split())
arr = [0] * N
arr[R - 1] = 1
count = 2
tree = [[] for _ in range(N)]
for _ in range(M):
    s, e = map(int, input().split())
    tree[s - 1].append(e - 1)
    tree[e - 1].append(s - 1)

for t in tree:
    t.sort(reverse=True)

move_list = [R - 1]
while move_list:
    now = move_list.pop()
    if not arr[now]:
        arr[now] = count
        count += 1
    now_line = tree[now]
    for i in now_line:
        if not arr[i]:
            move_list.append(i)

print(*arr)