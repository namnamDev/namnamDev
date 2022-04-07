a = int(input())
# 500000 7368787
size = 7368788
arr = [0] * size
arr[0] = 1
cnt = 0
an = 0
for i in range(2, size):
    if not arr[i]:
        cnt += 1
        if cnt == a:
            an = i
            break
        t = i * 2
        while t < size:
            arr[t] = 1
            t += i
print(an)