TT = int(input())
for T in range(1,TT+1) :
    N,M = map(int,input().split())
    print(N-M , M-(M//(2**N-1)%2))
    if (M-M//((2**N)-1))%2 :
        print(f"#{T} OFF")
    else:
        print(f"#{T} ON")
#0001 ----1 
#0010 ----2
#0011 ----3
#0100 ----4
#0101 ----5
#0110 ----6
#0111 ----7
#1111 ----15
#0001 0001
# if 8-1
# 30//2 15//2 7//2 3//2...1
#   1     0   0     0
# 10001
#2**n-1