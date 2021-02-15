# import sys
# sys.stdin = open("ExpertAcademy1493.txt")
T = int(input())
li = [(0,0)]
cnt = 0
#[(0,0), (1,1),/ (1,2), (2,1), /(1,3),(2,2),(3,1)/(1,4),(2,3),(3,2)(4,1)]
for i in range(1, T+1):
    p, q = map(int, input().split())
    while len(li) < q:
        for g in range(1,cnt):
            li += [(g, cnt-g)]
        cnt += 1
    temp = (li[p][0]+li[q][0],li[p][1]+li[q][1])

    temp_index = 0
    while temp not in li:
        for ff in range(1,cnt):
            li += [(ff, cnt-ff)]
        cnt += 1
    print("#{} {}".format(i,li.index(temp)))