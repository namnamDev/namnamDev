import sys
sys.stdin = open("Baekjoon10798.txt")
N = 5
li = [0]*N
maxLen = 0
an = ""
for i in range(N):
    li[i] = input()
    if maxLen < len(li[i]):
        maxLen = len(li[i])

for col in range(maxLen):
    for row in range(N):
        if len(li[row]) > col:
            an += li[row][col]

print(an)
