import sys

sys.stdin = open("ExpertAcademy1216.txt")
def Palin(words):
    for l in range(100, 0, -1):
        for k in range(100):
            for i in range(100 - l + 1):
                if words[k][i:i + l] == words[k][i + l - 1:i - 1:-1]:
                    print(words[k][i:i + l])
                    print(words[k][i + l - 1:i - 1:-1])
                    return l


for _ in range(1, 11):


    tc = int(input())
    words = [list(input()) for _ in range(100)]


    an = Palin(words)

    for i in range(100):
        for j in range(100):
            if i > j:
                words[i][j], words[j][i] = words[j][i], words[i][j]

    tmp = Palin(words)
    if an < tmp:
        an = tmp

    print("#{} {}".format(tc,an))
