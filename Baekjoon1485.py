import sys
sys.stdin = open("Baekjoon1485.txt")
T = int(input())
for i in range(1,T+1):
    square = [0] * 4
    templi = []
    an = 1
    for g in range(4):
        square[g] = tuple(map(int, input().split()))
        if g >= 1:
            print(square[g-1][0], square[g][0], square[g-1][1], square[g][1])
            templi += [(square[g-1][0]-square[g][0])**2+(square[g-1][1]-square[g][1])**2]
    print(square)
    templi += [(square[3][0]-square[0][0])**2+(square[3][1]-square[0][1])**2]
    print(square[3][0], square[3][1], square[0][0], square[0][1])
    print(templi)
    temp = templi[0]
    for f in templi:
        if temp != f:
            an = 0
            break
    print(an)
