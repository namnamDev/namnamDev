T = int(input())
cnt = 0
while T != 1:
    if T % 3 == 1:
        T -= 1
    elif T % 2 == 0:
        T //= 2
    else:
        T //= 3
    cnt += 1
print(cnt)
