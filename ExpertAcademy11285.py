import sys
sys.stdin = open("ExpertAcademy11285.txt")
T = int(input())
for i in range(1,T+1):
    TC = int(input())
    rounds = []
    score = 0
    # for r in range(1,11):
    #     rounds+=[r*20]
    # print(rounds)
    for g in range(TC):
        x,y = map(int,input().split())
        
        # x,y = abs(x),abs(y)
        # ban = (x+y)/2
        # for p in range(1,11):
        #     if ban >= 20*(11-(p+1)) and ban < 20*(11 - p):
        #         score+=p
        #         break
    print("#{} {}".format(i,score))


