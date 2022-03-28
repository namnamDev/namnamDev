import sys

sys.stdin = open("Baekjoon4948.txt")
size = 123456
arr = [0] * (size * 2 + 1)
for i in range(2, size):
    if not arr[i]:
        temp = i
        while temp <= size * 2:
            arr[temp] = 1
            temp += i
        arr[i] = 0
while True:
    a = int(input())
    if not a:
        break
    cnt = 0
    for aa in range(a + 1, a * 2 + 1):
        if not arr[aa]:
            cnt += 1
    print(cnt)
