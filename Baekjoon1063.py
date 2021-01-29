def R(x,y):
    return x,y+1
def L(x,y) :
    return x,y-1
def B(x,y) :
    return x-1,y
def T(x,y):
    return x+1,y
def RT(x,y):
    return x+1,y+1
def LT(x,y):
    return x+1,y-1
def RB(x,y):
    return x-1,y+1
def LB(x,y):
    return x+1,y-1

# board = [[0 for i in range(8)] for i in range(8)]
# print(board)
move_dict = {'R':R , 'L':L , 'B':B , 'T':T , 'RT':RT , 'LT':LT, 'RB':RB , 'LB':LB}
T = input().split()
king = ((ord(T[0][0])-65),int(T[0][1]))
stone = ((ord(T[1][0])-65),int(T[1][1]))
N = int(T[2])
moveList = []
for case in range(N):
    moves = input()
    moveList.append(moves)
# print(king, stone , N , moveList)
for move in moveList:
    king_will = move_dict.get(move)(*king)
    print(king_will)
    print(move)
    if king_will[0]>0 and king_will[1]>0 and king_will[0]<8 and king[1]<8:
        king = king_will
        print(king)
        # print('이동방해')
    if king_will == stone :
        stone = move_dict.get(move)(*stone)
fin_king = chr(king[0]+65)+str(king[1])
fin_stone = chr(stone[0]+65)+str(stone[1])
print(fin_king, king)
print(fin_stone,stone)