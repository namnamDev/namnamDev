import sys

sys.stdin = open("Baekjoon11054.txt")

N = int(input())
arr = list(map(int, input().split()))
dp_left = [1] * N
dp_right = [1] * N
for fir in range(N):
    for sec in range(fir - 1, -1, -1):
        if arr[fir] > arr[sec]:
            dp_left[fir] = max(dp_left[fir], dp_left[sec] + 1)
        # if arr[fir] < arr[sec]:
        #     dp_right[fir] = max(dp_right[fir], dp_right[sec] + 1)
max_val = 0
for f in range(N - 1, -1, -1):
    for s in range(f + 1, N, 1):
        if arr[f] > arr[s]:
            dp_right[f] = max(dp_right[f], dp_right[s] + 1)
    max_val = max(dp_right[f] + dp_left[f], max_val)
print(max_val - 1)
