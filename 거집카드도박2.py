import random

# 카드 0이 될때까지 돌리자
T, C = map(int, input().split())  # 내가 가진 갯수, 회당 돌릴갯수
maxCard = 8
tMin = 0
tMax = maxCard if C >= 4 else C * 2
cntList = []
Adds = Mids = Loses = 0
for i in range(100):
    tAdd = 0
    tMid = 0
    tLose = 0
    nowIhave = T
    cnt = 0
    while nowIhave >= C:
        nowIhave -= 4
        printed = random.randrange(tMin, tMax + 1)
        nowIhave += printed
        cnt += 1
    if nowIhave < T:
        tLose += 1
        Loses += 1
    elif nowIhave > T:
        tAdd += 1
        Adds += 1
    else:
        tMid += 1
        Mids += 1
    cntList.append(cnt)
    print("cnt :", cnt, "result :", tLose, tMid, tAdd)
print("avgCnt :", sum(cntList) / 100, "result :", Loses, Adds)
