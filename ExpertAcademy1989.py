import sys

sys.stdin = open("ExpertAcademy1989.txt")
for tc in range(1, int(input()) + 1):
    a = input()
    an = 0
    lenA = len(a)
    for i in range(lenA // 2):
        if a[i] != a[lenA - i - 1]:
            break

        if i == lenA // 2 - 1:
            an = 1
    print("#{} {}".format(tc, an))
