X, Y = map(int, input().split())
Z = int((Y / X * 100))
cnt = 0
if X != Y:
    while int((Y + cnt) / (X + cnt) * 100) == Z:
        cnt += 1
else:
    cnt = -1
print(X - Y)
print(cnt)
