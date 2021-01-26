answer = []
T = int(input())
for case in range(T):
    NM = list(map(int, input().split()))
    N = NM[0]
    M = NM[1]
    boards = []
    for line in range(N) :
        lines = list(map(int, input().split()))
        boards.append(lines)
    # print(boards)
    maxs = 0
    for start in range(N-M+1):
        for kills in range(N-M+1):
            temp = 0
            for i in range(M):
                for g in range(M):
                    temp += boards[start + g][kills + i]
                    # print(start + i, kills + g,boards[start + g][kills + i])
            if maxs < temp :
                maxs = temp
            # print('---' + str(temp))
    answer.append(maxs)

for i in range(T):
    print(f'#{i+1} {answer[i]}')