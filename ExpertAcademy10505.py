import sys
sys.stdin = open("ExpertAcademy10505.txt")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    li = list(map(int,input().split()))
    sums = 0
    for i in li:
        sums += i
    avg = sums/N
    cnt = 0
    for g in li:
        if g <= avg:
            cnt += 1
    print("#{} {}".format(tc, cnt))



    # leftList, rightList = [0]*N, [0]*N
    # for i in range(N):
    #     leftList[i], rightList[i] = map(int, input().split())
    # print(leftList,rightList)
    # print('#{} {}'.format(tc, a))
