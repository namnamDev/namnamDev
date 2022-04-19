vi = [0] * 10001
arr = list(range(1, 10001))
while arr:
    n = arr.pop()
    t = n + sum(list(map(int, str(n))))
    if t < 10001 and not vi[t]:
        vi[t] = 1
        arr.append(t)
for i in range(1, 10001):
    if not vi[i]:
        print(i)