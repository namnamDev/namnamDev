import sys

sys.stdin = open("ExpertAcademy4366.txt")

for tc in range(int(input())):
    two = list(input())
    three = list(input())
    two_set = set()
    three_set = set()
    an = 0
    for i in range(len(two)):
        temp2 = two.copy()
        temp2[i] = str(abs(int(temp2[i]) - 1))
        two_set.add(int(''.join(temp2), 2))

    for g in range(len(three)):
        for i in range(3):
            temp3 = three.copy()
            if temp3[g] != str(i):
                temp3[g] = str(i)
                tempint3 = int(''.join(temp3), 3)
                three_set.add(tempint3)

    for i in two_set:
        for f in three_set:
            if i == f:
                an = i
                break
    print("#{} {}".format(tc + 1, an))
