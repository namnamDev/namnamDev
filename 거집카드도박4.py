import random

# 희망 목표 갯수가 +1~ *2까지
T, C = map(int, input().split())  # 내가 가진 갯수, 회당 돌릴갯수, 희망 갯수
maxCard = 8
tMin = 0
tMax = maxCard if C >= 4 else C * 2
hope = T * 2
for H in range(T + 1, T * 2 + 1):
    vi = [0] * (H + 11)
    win = 0
    lose = 0
    mid = 0
    for i in range(10000):
        nowIhave = T
        cnt = 0
        while C <= nowIhave <= H:
            nowIhave -= C
            printed = random.randrange(tMin, tMax + 1)
            nowIhave += printed
            cnt += 1
        vi[nowIhave] += 1
        if H < nowIhave:
            win += 1
        elif H > nowIhave:
            lose += 1
        else:
            mid += 1
    # print(nowIhave, cnt)
    print("Hope : ", H, "result :", lose / 100, win / 100)
