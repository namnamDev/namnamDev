import random

# 초기 카드를 T*C만큼 가지고 있다고 가정
T, C = map(int, input().split())  # 횟수, 한번당 넣을갯수
maxCard = 8
tMin = 0
tMax = maxCard if C >= 4 else C * 2
print(tMin, tMax)
tAdd = 0
tMid = 0
tLose = 0

for tc in range(100):
    total = 0
    vi = [0] * (maxCard + 1)
    for i in range(T):
        vi[random.randrange(tMin, tMax + 1)] += 1
    for i in range(maxCard):
        total += vi[i] * i
    total -= T * C
    print(vi, total)
    if total < 0:
        tLose += 1
    elif total > 0:
        tAdd += 1
    else:
        tMid += 1
print(tLose, tAdd)
