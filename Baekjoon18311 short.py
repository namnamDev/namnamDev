NK = list(map(int, input().split()))
N , K = NK[0],NK[1]
course = list(map(int, input().split()))
total = sum(course)
K = total-K if K>total else K
sums = 0
cnt = 0
if K>=0:
    while sums <= K :
        sums+=course[cnt]
        cnt+=1
    print(cnt)
else :
    cnt = 1
    while sums > K :
        sums-=course[-cnt]
        cnt+=1
        # print(K,N-cnt+2,course[-cnt],sums)
    print(N-cnt+2)