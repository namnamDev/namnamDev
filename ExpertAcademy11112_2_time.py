import sys

sys.stdin = open("ExpertAcademy11112.txt")
for tc in range(1, int(input()) + 1):
    p, q, r = map(int, input().split())
    a, b, c, d = map(int, input().split())
    li = [(a, b), (a, d), (c, b), (c, d)]
    # li = [(p - i[a]) ** 2 + (q - i[b]) ** 2,(p - i[a]) ** 2 + (q - i[d]) ** 2,(p - i[c]) ** 2 + (q - i[1]) ** 2]
    red = "Y"
    blue = "Y"
    maxLen = 0
    maxIdx = 0
    while True:
        for i in li:
            temp = (p - i[0]) ** 2 + (q - i[1]) ** 2
            if maxLen < temp:
                maxLen = temp
                maxIdx = i
        if maxLen <= r ** 2:
            print("#{} YN".format(tc))
            break

        if a < p < c and b < q < d:
            arr = [p - a, c - p, q - b, d - q]
            minvalue = min(arr)
            if r <= minvalue:
                red = "N"
                print("#{} NY".format(tc))
                break
