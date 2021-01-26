T = int(input())
for case in range(1,T+1):
    N = int(input())
    print(f'#{case} {(-((N-1)//2)+N) if N%2==1 else -(N//2)}')