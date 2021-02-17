import sys
sys.stdin = open("ExpertAcademy2001.txt")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [0]*N
    for i in range(N):
        board[i] = list(map(int, input().split()))
    kills = 0
    for f in range(N-M+1):
        for ff in range(N-M+1):
            temp = 0
            for g in range(f, f+M):
                for gg in range(ff, ff+M):
                    temp += board[g][gg]
            if temp > kills:
                kills = temp
    print("#{} {}".format(tc, kills))


