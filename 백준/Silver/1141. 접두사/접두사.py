a = int(input())
arr = [input() for _ in range(a)]
arr.sort()
visit = [0] * a
for i in range(a - 1):
    if arr[i] == arr[i + 1][:len(arr[i])]:
        visit[i] = 1
print(visit.count(0))