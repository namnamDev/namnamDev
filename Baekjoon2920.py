import sys

sys.stdin = open('Baekjoon2920.txt')
ar = list(map(int, input().split()))
ac = 1
dc = 8
an = ""
if ar[0] != 1 and ar[0] != 8:
    an = 'mixed'
else:
    t = ar[0]
    if t == 1:
        for i in range(len(ar) - 1):
            if ac == ar[i]:
                ac += 1
            else:
                an = 'mixed'
                break
        if ac == 8:
            an = 'ascending'
    elif t == 8:
        for i in range(len(ar) - 1):
            if dc == ar[i]:
                dc -= 1
            else:
                an = 'mixed'
                break
        if dc == 1:
            an = 'descending'
print(an)
