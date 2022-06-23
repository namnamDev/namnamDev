N = int(input())
a = input()
dict = {"R": 0, "B": 0}
now = a[0]
for one in range(1, N):
    if now != a[one]:
        dict[now] += 1
        now = a[one]
dict[now] += 1
print(min(dict["R"], dict["B"]) + 1)