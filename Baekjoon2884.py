H, M = map(int, input().split())
bef = M - 45
if bef < 0:
    bef += 60
    H -= 1
if H < 0:
    H += 24

print('{} {}'.format(H, bef))
