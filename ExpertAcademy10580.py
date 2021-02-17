import sys
sys.stdin = open("ExpertAcademy10580.txt")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    li = [0]*N
    cnt = 0
    for i in range(N):
        li[i] = tuple(map(int,input().split()))
        for g in range(i):
            if (li[i][0] < li[g][0] and li[i][1] > li[g][1]) or (li[i][0] > li[g][0] and li[i][1] < li[g][1]):
                cnt += 1
    print("#{} {}".format(tc, cnt))


    # leftList, rightList = [0]*N, [0]*N
    # for i in range(N):
    #     leftList[i], rightList[i] = map(int, input().split())
    # print(leftList,rightList)
    # print('#{} {}'.format(tc, a))
