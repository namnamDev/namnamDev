import sys
def inputs():
    return sys.stdin.readline()

def inli() :
    return list(map(int,(inputs().split())))

NM = inli()
N , M = NM[0], NM[1]
board = []
for i in range(N):
    board += [inli()]
S = int(inputs())
anlist = [] 
for i in range(S):
    ra = inli()
    p1 = (ra[0]-1,ra[1]-1)
    p2 = (ra[2]-1,ra[3]-1)
    sums = 0 
    for i in range(p1[0],p2[0]+1):
        for g in range(p1[1],p2[1]+1):
            sums +=board[i][g]
    anlist+=[sums]
for i in anlist:
    print(i)