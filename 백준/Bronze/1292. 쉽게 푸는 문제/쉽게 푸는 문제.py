A, B = map(int, input().split())
total = 0
arr = []
idx = 0
num = 1
while len(arr) < 1000:
    temp = [num] * num
    arr += temp
    num += 1
for i in range(A - 1, B):
    total += arr[i]

print(total)