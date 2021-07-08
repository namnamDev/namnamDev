N, M = map(int, input().split())
# A = 1
# B = M
idx = 0
cnt = 1
an = 1
for i in range(1, N // M):
    temp = 1
    for g in range(1, i):
        temp *= g
    for f in range()
# N=5 M=2
# AAAAA 54321/54321
# BAAA 4321 321
# ABAA
# AABA
# AAAB
# BBA 321 21
# BAB
# ABB
#N=7 M=3
#AAAAAAA
#BAAAA 5(N-M+1)
#ABAAA
#AABAA....
#BBA3(N//M+1)