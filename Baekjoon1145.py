import sys

sys.stdin = open("Baekjoon1145.txt")
arr = sorted(list(map(int, input().split())))
an = 0
i = 1
while not an:
    cnt = 0
    for ii in range(5):
        if not i % arr[ii]:
            cnt += 1
    if cnt >= 3:
        an = i
        break
    i += 1
print(an)
