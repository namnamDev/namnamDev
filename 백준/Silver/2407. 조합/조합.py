a, b = map(int, input().split())
aa = 1
for t in range(b):
    aa *= a
    a -= 1
bb = 1
for t in range(1, b + 1):
    bb *= t
print(aa // bb)