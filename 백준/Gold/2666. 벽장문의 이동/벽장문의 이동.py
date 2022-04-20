def findDoor(pA, pB, pIdx, pMove):
    if pIdx == M:
        global an
        an = min(an, pMove)
        return
    now = suns[pIdx]
    disA = abs(pA - now)
    disB = abs(pB - now)
    findDoor(now, pB, pIdx + 1, pMove + disA)
    findDoor(pA, now, pIdx + 1, pMove + disB)


N = int(input())
a, b = map(int, input().split())
a -= 1
b -= 1
M = int(input())
suns = [int(input()) - 1 for _ in range(M)]
an = N * M
findDoor(a, b, 0, 0)
print(an)
