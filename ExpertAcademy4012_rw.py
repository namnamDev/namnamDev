import sys

sys.stdin = open("ExpertAcademy4012.txt")


def powerset(arr):  # 첫번째 음식의 재료 부분집합을 구할 함수
    global minis
    if len(arr) == N // 2:
        tempUse = []  # 두번째 음식 재료를 담을 리스트
        f1 = 0  # 첫번쨰 음식의 총 합을 넣을 변수
        f2 = 0  # 두번째 음식의 총합을 넣을 변수
        for i in range(N):  # 첫번쨰음식에서 사용하지 않은 재료가 모두 두번쨰 음식에 들어가므로
            if used[i] == 0:  # used에서 0인것들을 찾아
                tempUse += [i]  # tempUse에 넣어줌.

        for i in range(N // 2):  # 재료 list의 부분집합
            for g in range(i + 1, N // 2):  # 각 재료별 총합을 구하기 위함. 재료 갯수만큼 하되 두번 더함.
                f1 += board[arr[i]][arr[g]] + board[arr[g]][arr[i]]  #
                f2 += board[tempUse[i]][tempUse[g]] + board[tempUse[g]][tempUse[i]]

        minis += [abs(f1 - f2)]  # 최소값을 담는 list에다 원소를 추가해주고, 출력에서는 min함수 활용.
        return
    else:
        for i in range(N):
            if used[i] == 0:  # 재료가 한번도 사용된적이 없을때
                if len(arr):  # arr에 변수가 최소 하나라도 있을때
                    if i > arr[len(
                            arr) - 1]:  # i가 arr의 최후 값보다 클때에만 재귀함. 부분집합에서는 1,2,3 / 2,1,3 / 3,2,1 다 다르지만 이 문제에서는 다 같으므로 불필요한 반복 배제.
                        used[i] = 1
                        powerset(arr + [i])
                        used[i] = 0  # powerset알고리즘
                else:  # arr에 아무 변수도 없을때에는 값 추가해서 넘김.
                    used[i] = 1
                    powerset(arr + [i])
                    used[i] = 0


for tc in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N  # ==visited랑 같은 용도
    minis = []  # 음식의 차이를 넣을 리스트
    powerset([])
    print("#{} {}".format(tc + 1, min(minis)))
