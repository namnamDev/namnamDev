import sys

sys.stdin = open("ExpertAcademy11112.txt")
for tc in range(1, int(input()) + 1):
    p, q, r = map(int, input().split())
    a, b, c, d = map(int, input().split())
    pp = (p, q)
    li = [(a, b), (a, d), (c, b), (p, q)]
    red = "Y"
    blue = "Y"
    maxLen = 0
    maxIdx = 0
    for i in li:
        temp = (p - i[0]) ** 2 + (q - i[1]) ** 2
        if maxLen < temp:
            maxLen = temp
            maxIdx = i

    if maxLen <= r ** 2:
        blue = "N"

    if a < p < c and b < q < d:
        arr = [p - a, c - p, q - b, d - q]
        minvalue = min(arr)
        if r <= minvalue:
            red = "N"
    print("#{} {}{}".format(tc, red, blue))
