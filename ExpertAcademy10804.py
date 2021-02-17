import sys
sys.stdin = open("ExpertAcademy10804.txt")
#qppdb
#pqqbd
T = int(input())
for tc in range(1,T+1):
    N = input()
    a = ""
    for i in N:
        temp = ""
        if i == "b":
            temp = "d"
        elif i =="d":
            temp = "b"
        elif i == "p":
            temp = "q"
        else:
            temp = "p"
        a = temp+a
    print('#{} {}'.format(tc, a))
