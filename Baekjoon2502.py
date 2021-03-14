def pibo(N):
    if N < 2:
        return arr[N]

    if arr[N - 1] and arr[N - 2]:
        arr[N] = [0, 0]
        arr[N][0] = arr[N - 1][0] + arr[N - 2][0]
        arr[N][1] = arr[N - 1][1] + arr[N - 2][1]
        return
    else:
        if not arr[N - 1]:
            pibo(N - 1)
        if not arr[N - 2]:
            pibo(N - 2)


D, K = map(int, input().split())
arr = [0] * (D + 1)
arr[0] = [1, 0]
arr[1] = [0, 1]
pibo(D + 1)
x = arr[D - 1][0]
y = arr[D - 1][1]
n = 0
m = 0
while x * n + y * m != K:
    n += 1
    if not (K - x * n) % y:
        m = (K - x * n) // y
        break
print(n)
print(m)
