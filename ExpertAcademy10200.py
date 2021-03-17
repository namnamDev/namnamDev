import sys

sys.stdin = open("ExpertAcademy10200.txt")
T = int(input())
for tc in range(1, T + 1):
    N, A, B = map(int, input().split())
    ms = A if A <= B else B
    minis = A + B - N if N < A + B else 0

    print("#{} {} {}".format(tc, ms, minis))

    # leftList, rightList = [0]*N, [0]*N
    # for i in range(N):
    #     leftList[i], rightList[i] = map(int, input().split())
    # print(leftList,rightList)
    # print('#{} {}'.format(tc, a))
