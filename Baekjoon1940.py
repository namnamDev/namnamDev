import sys
N = int(input())
M = int(input())
NS = list(map(int, input().split()))
cnt = 0
# NS.sort()
for i in range(N):
    if (M-NS[i]) in NS:
        cnt += 1
    # for g in range(i+1, N):
    #     if NS[i]+NS[g] == M:
    #         cnt += 1
    #         break
        # if NS[i]+NS[g] >M:
        #     break
print(cnt//2)