T  = int(input())
# NM = list(map(int , input().split()))
# N = NM[0]
# M = NM[1]
# A = list(map(int , input().split()))
# B = list(map(int , input().split()))
# if(M<N) :
#     A,B = B,A
# max = 0
# for i in range(len(B) - len(A)+1): ## 여기 1을 더해주지않으면 마지막 바퀴 시행 X
#     temp = 0
#     for g in range(len(A)) :
#         temp += A[g]*B[i+g]

#     if(max< temp):
#         max = temp

# print(max)
for case in range(1,T+1):
    NM = list(map(int , input().split()))
    N = NM[0]
    M = NM[1]
    A = list(map(int , input().split()))
    B = list(map(int , input().split()))
    if(M<N) :
        A,B = B,A
    maxs = 0
    for i in range(len(B) - len(A)+1): ## 여기 1을 더해주지않으면 마지막 바퀴 시행 X
        temp = 0
        for g in range(len(A)) :
            temp += A[g]*B[i+g]

        if(maxs< temp):
            maxs = temp
    print(f'#{case} {maxs}')