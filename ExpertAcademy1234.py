import sys
sys.stdin = open("ExpertAcademy1234.txt")

for i in range(1, 11):
    N, li = input().split()
    li = list(li)
    an = ""
    for f in li:
        an += f
        if len(an) >= 2 and an[-1] == an[-2]:
            an = an[:-2]
    print("#{} {}".format(i, an))


