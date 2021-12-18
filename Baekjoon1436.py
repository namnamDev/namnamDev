import sys

sys.stdin = open('Baekjoon1436.txt')

# def ma(strN, cnt):
#     if cnt == N:
#         print(strN)
#         return
#
#     if int(strN[0]) < 6:
#         ma(str(int(strN[0]) + 1) + strN[1:], cnt + 1)
#     elif int(strN[-1]) > 6:
#         ma(strN[:-1] + str(int(strN[-1]) + 1), cnt + 1)
#     else:
#         ma("1" + strN, cnt + 1)


N = int(input())

cnt = 1
strN = "666"
# while cnt < N:
#     if int(strN[0]) < 5:
#         strN = str(int(strN[0]) + 1) + strN[1:]
#     elif int(strN[0]) > 6:
#         strN = strN[:-1] + str(int(strN[-1]) + 1)
#     else:
#         strN = "1" + strN
#     cnt += 1
#     print(strN)
# print(strN)
while cnt < N:
    addNB = addF = "1" + strN
    addNF = addB = strN + "1"
    if len(strN) > 3:
        addNF = str(int(strN[0]) + 1) + strN[1:]
        addNB = strN[:-1] + str(int(strN[-1]) + 1)
    strN = str(min(int(addF), int(addB), int(addNF), int(addNB)))
    cnt += 1
    print(int(addF), int(addB), int(addNF), int(addNB))
    print(strN)
# 1666 2666 3666 ... 5666
# 6661 6662 6663 ... 6666
# 11666 12666 13666 14666 .... 15666
# 16661 16662 16663 16664 ...  16666
# 16666 26666 36666.... 56666
