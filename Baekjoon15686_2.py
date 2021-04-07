import sys

sys.stdin = open('Baekjoon15686.txt')


def powerset(index, arr):
    global Chickens
    if index == len(C):
        if len(arr) == M:
            Chickens += [arr]
        return

    if len(arr) == M:
        Chickens += [arr]
        return
    else:
        powerset(index + 1, arr + [C[index]])
        powerset(index + 1, arr)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
Q = []
C = []
for i in range(N):
    for g in range(N):
        if board[i][g] == 1:
            Q.append([i, g])
        elif board[i][g] == 2:
            C.append([i, g])
Chickens = []
powerset(0, [])
tempABS = [[]] * len(Q)

result = []
for chicken in Chickens:
    temp_result = 0
    for i in range(len(Q)):
        temp = []
        for chick in chicken:
            temp += [abs(Q[i][0] - chick[0]) + abs(Q[i][1] - chick[1])]
        temp_result += min(temp)
    result += [temp_result]

print(min(result))
