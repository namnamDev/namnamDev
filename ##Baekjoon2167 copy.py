import sys
def inputs():
    return sys.stdin.readline()

def inli() :
    return list(map(int,(inputs().split())))

N , M  = inli()
board = []
for i in range(N):
    board += [inli()]
anlist = [] 
dp = [[0]*(M+1)for g in range(N+1)] 
for i in range(1,N+1):
    for g in range(1,M+1):
        dp[i][g] = board[i-1][g-1] + dp[i][g-1] + dp[i-1][g] - dp[i-1][g-1]
S = int(inputs())
for _ in range(S):
    x1,y1,x2,y2 = inli()
    an = dp[x2][y2] -dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(an)