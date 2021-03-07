A, B = map(int, input().split())


def dfs(a, zer, move):
    global cnt
    if a == B - 1:
        print("here", a, zer, move)
        if zer < cnt:
            cnt = zer
        return
    for i in range(3):
        wa = a + move + dirx[i]
        if a < wa < B:
            print(wa, zer + 1, move + dirx[i])
            dfs(wa, zer + 1, move + dirx[i])


dirx = [-1, 0, 1]
cnt = B - A
B = B - A
A = 0
# print(A, B)
dfs(A, 0, 1)
print(cnt + 1)
