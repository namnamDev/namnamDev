N, M = map(int, input().split())
arr = list(map(int, input().split()))
an = 0
for fir in range(N):
    temp_num = arr[fir]
    idx = fir + 1
    while temp_num < M:
        if idx == N:
            break
        temp_num += arr[idx]
        idx += 1
    if temp_num == M:
        an += 1
print(an)
