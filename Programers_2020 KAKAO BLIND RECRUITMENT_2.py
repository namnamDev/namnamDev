def cycle(arr):
    N = len(arr)
    board = [[0] * N for _ in range(N)]
    for i in range(N):
        for h in range(N):
            one = arr[i][h]
            board[h][N - 1 - i] = one
    return board


def solution(key, lock):
    # key = [[1,1,1],[1,1,1],[1,1,1]]
    # lock = [[0,0,0,],[0,0,0],[0,0,0]]
    N, M = len(key), len(lock)
    # print('key')
    # for i in key:
    #     print(i)
    # print('lock')
    # for g in lock:
    #     print(g)
    answer = False
    for f in range(4):
        key = cycle(key)
        Q = []
        for i in range(N):
            for g in range(N):
                if key[i][g]:
                    Q += [[i, g]]
        # print(Q)
        for ii in range(-M + 1, M):
            for gg in range(-M + 1, M):
                temp = [[0] * M for _ in range(M)]

                for i in range(M):
                    for g in range(M):
                        temp[i][g] = lock[i][g]

                for qq in Q:
                    keyy, keyx = qq[0], qq[1]
                    if 0 <= ii + keyy < M and 0 <= gg + keyx < M:
                        if temp[ii + keyy][gg + keyx]:
                            break
                        else:
                            temp[ii + keyy][gg + keyx] = 1
                # print(ii,gg,temp)
                cnt = 0
                for i in temp:
                    if 0 not in i:
                        cnt += 1

                if cnt == M:
                    answer = True
                    break
            if answer:
                break
        if answer:
            break
    return answer
