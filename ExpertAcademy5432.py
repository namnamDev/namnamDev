import sys
sys.stdin = open("ExpertAcademy5432.txt")
T = int(input())
for tc in range(1,T+1):
    bar = input()
    s = []
    cnt = 0
    for i in range(len(bar)):
        if bar[i] == "(":
            s += ["("]
        else:
            s.pop()
            if bar[i-1] == "(":
                cnt += len(s)
            else:
                cnt += 1
    print("#{} {}".format(tc, cnt))

