def dfs(a, zer, move):
    global cnt
    if a == B - 1:
        if zer < cnt:
            cnt = zer
        return
    for i in range(3):
        wa = a + move + dirx[i]
        if a < wa < B:
            dfs(wa, zer + 1, move + dirx[i])


A, B = map(int, input().split())
dirx = [-1, 0, 1]
cnt = B - A
B = B - A
A = 0
dfs(A, 0, 1)
print(cnt + 1)
