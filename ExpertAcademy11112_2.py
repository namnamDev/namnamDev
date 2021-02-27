import sys

sys.stdin = open("ExpertAcademy11112.txt")
for tc in range(1, int(input())):
    p, q, r = map(int, input().split())
    a, b, c, d = map(int, input().split())
    aa = (a, b)
    bb = (a, d)
    cc = (c, b)
    dd = (c, d)
    red = ""
    blue = ""
    if a < p < c and b < q < d:
        if p + r < c and p - r < a and q + r < d and q - r < b:
            red = "N"
        else:
            red = "Y"
        blue = "Y"
    elif p < (a + c) / 2 and q < b:
        if (p - c) ** 2 + (q - d) ** 2 < r ** 2:
            blue = "N"

    x = 0
    y = 0
    # b
    # d
    # ac
