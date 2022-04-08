import sys
T = int(input())
size = 1000001
arr = [1] * size
for i in range(2, size):
    t = i
    while t < size:
        arr[t] += i
        t += i
    arr[i] += arr[i - 1]
for _ in range(T):
    a = int(sys.stdin.readline())
    print(arr[a])
