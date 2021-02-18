import sys
sys.stdin = open("ExpertAcademy4861.txt")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    li = [0]*N
    for i in range(N):
        li[i] = list(input())
    an = ""
    c = 0
    while c < N and an == "":
        for i in range(N - M + 1):
            temp = li[c][i:i+M]
            # print(temp)
            for g in range(M//2):
                if temp[g] != temp[-g-1]:
                    break
                if g == M//2-1:
                    an = temp
        c += 1
    c = 0
    while c < N and an == "":
        for i in range(N - M + 1):
            temp = []
            for gg in range(i,i+M):
                temp += [li[gg][c]]
            for g in range(M//2):
                if temp[g] != temp[-g-1]:
                    break
                if g == M//2-1:
                    an = temp
        c += 1
    answer = "".join(an)
    print("#{} {}".format(tc, answer))

