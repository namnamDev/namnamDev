import sys

sys.stdin = open('Baekjoon1195.txt')
fir = list(map(int, input()))
sec = list(map(int, input()))
if len(fir) < len(sec):
    fir, sec = sec, fir
an = len(fir) + len(sec)

for f1 in range(len(fir) - len(sec) + 1):
    for s1 in range(len(sec)):
        if fir[s1 + f1] == "2" and sec[s1] == "2":
            break
        if s1 == len(sec) - 1:
            an = len(fir)
if an == len(fir) + len(sec):
    idx = 1
    while idx < len(fir):  # 왼쪽
        leftSlice = sec[idx:]
        rightSlice = sec[:len(sec) - idx]
        for ff in range(len(leftSlice)):
            if leftSlice[ff] == 2 and fir[ff] == 2:
                break
            if ff == len(leftSlice) - 1:
                an = len(fir) + idx

        for fff in range(len(rightSlice)):
            if rightSlice[fff] == 2 and fir[len(fir) - len(rightSlice) + fff] == 2:
                break
            if fff == len(rightSlice) - 1:
                an = len(fir) + idx
        idx += 1
        if an != len(fir) + len(sec):
            break
print(an)
