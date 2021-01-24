import sys
T = int(input())
for i in range(T):
    S = sys.stdin.readline().split()
    cnt = int(S[0])
    answer = ''
    for g in S[1]:
        answer += g*cnt
    
    print(answer)
