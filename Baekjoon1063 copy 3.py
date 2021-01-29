def R(x,y):
    return x+1,y
def L(x,y) :
    return x-1,y
def B(x,y) :
    return x,y-1
def T(x,y):
    return x,y+1
def RT(x,y):
    return x+1,y+1
def LT(x,y):
    return x-1,y+1
def RB(x,y):
    return x+1,y-1
def LB(x,y):
    return x-1,y-1

move_dict = {'R':R , 'L':L , 'B':B , 'T':T , 'RT':RT , 'LT':LT, 'RB':RB , 'LB':LB}
T = input().split()
king = ((ord(T[0][0])-64),int(T[0][1]))
stone = ((ord(T[1][0])-64),int(T[1][1]))
N = int(T[2])
moveList = []
for case in range(N):
    moves = input()
    moveList.append(moves)

for move in moveList:
    king_will = move_dict.get(move)(*king)
    if 0 < king_will[0]<=8 and 0 < king_will[1] <=8 : 
        if king_will == stone :
            stone_will = move_dict.get(move)(*stone)
            if 0 < stone_will[0]<=8 and 0 < stone_will[1]<=8: 
                stone = stone_will
                king = king_will
        else : 
            king = king_will
fin_king = chr(king[0]+64)+str(king[1])
fin_stone = chr(stone[0]+64)+str(stone[1])
print(fin_king)
print(fin_stone)