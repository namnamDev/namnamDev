import sys

sys.stdin = open('Baekjoon10799.txt')
wood = input()
print(wood)
S = []
cnt = 0
depth = 0
for i in wood:
    if i == ")":
        temp = S.pop()
        cnt += len(S)
        print(len(S), S, cnt)
    else:
        S.append(i)
    # if not S:
    #     cnt += 1
print(S)
print(cnt)
