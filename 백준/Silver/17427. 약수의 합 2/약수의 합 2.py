T = int(input())
arr = [1] * (T + 1)
arr[0] = 0
for i in range(2, T + 1):
    t = i
    while t < T + 1:
        arr[t] += i
        t += i
print(sum(arr))