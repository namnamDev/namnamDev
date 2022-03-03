import random

T = int(input())  # 내가 가진 갯수, 회당 돌릴갯수, 희망 갯수
maxCard = 8
tMin = 0
hope = T * 2
for C in range(1, maxCard):
    tMax = maxCard if C >= 4 else C * 2
    print(tMin, tMax)
    for H in range(T + 1, T * 2 + 1):
        vi = [0] * (H + 11)
        win = 0
        lose = 0
        mid = 0
        aa = []
        bb = []
        for i in range(1000):
            nowIhave = T
            cnt = 0
            while C <= nowIhave < H:
                nowIhave -= C
                printed = random.randrange(tMin, tMax + 1)
                nowIhave += printed
                aa.append(nowIhave)
                bb.append(printed)
                cnt += 1
            vi[nowIhave] += 1
            if H <= nowIhave:
                win += 1
            elif H > nowIhave:
                lose += 1
            else:
                mid += 1
        # print(nowIhave, cnt)
        print("cnt :", C, "Hope : ", H, "result :", lose, win)
