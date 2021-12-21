import sys

sys.stdin = open('Baekjoon9207.txt')
T = int(input())
allBoard = []
for tc in range(T - 1):
    tempBoard = []
    while True:
        a = input()
        if a:
            al = list(a)
            tempBoard.append(al)
        else:
            break
    allBoard.append(tempBoard)
print(allBoard)
firY = len(allBoard[0])
firX = len(allBoard[0][0])
tempBoard2 = [list(input()) for _ in range(firY)]
allBoard.append(tempBoard2)
