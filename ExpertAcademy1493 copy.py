# import sys
# sys.stdin = open("ExpertAcademy1493.txt")
T = int(input())
li = [[1], [2, 3], [4, 5, 6]]
for i in range(1, T+1):
    p, q = map(int, input().split())
    while li[-1][-1] < q:
        temp = []
        last = li[-1][-1]
        for f in range(1, len(li[-1])+2):
            temp += [last+f]
        li += [temp]
    print(li)
    col = 0
    rows = 0
    for g in range(len(li)):
        for h in range(len(li[g])):
            if li[g][h] == p:
                rows = g
                col = h
                break

    temps = [rows+1, col+1]

    col = 0
    rows = 0
    for g in range(len(li)):
        for h in range(len(li[g])):
            if li[g][h] == q:
                rows = g
                col = h
                break
    temps2 = [rows+1, col+1]

    print(temps, temps2)
    x = temps[0]+temps2[0]
    y = temps[1]+temps2[1]
    # print(temps[0]+temps2[0])
    # print(temps[1]+temps2[1])
    print(li[x][y])
