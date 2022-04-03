a, b = map(int, input().split())
arr = [0] * (b + 1)
arr[0] = arr[1] = 1
for i in range(2, b + 1):
    if not arr[i]:
        t = i * 2
        while t <= b:
            arr[t] = 1
            t += i
for i in range(a, b + 1):
    if not arr[i]:
        print(i)