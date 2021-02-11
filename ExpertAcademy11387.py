import sys
sys.stdin = open("ExpertAcademy11387.txt")

T = int(input())
for i in range(1,T+1):
    D,L,n = map(int,input().split())
    #an = D*N + D*(0+L%+2L%*+..n-1L%)
    #an = D*N + (n(n-1)/2)L/100
    sums = int(n*(n-1)/2)
    # print(sums,L)
    # print(sums*L)
    # print(sums*L/100)
    # print(sums*L/100)
    # print(n+sums*L/100,D)
    # print(D*(n+sums*L/100))
    # print((D*(n+sums*L/100)*10))
    # print(int((D//100*(n+sums*L)*10))//10)
    # print((D*(n+sums*L/100)))
    # print(D*n + D//100*sums*L)
    # for g in range(N-1):
    #     sums += (D*(1+N*L/100))
    print("#{} {}".format(i,D*n + D//100*sums*L))