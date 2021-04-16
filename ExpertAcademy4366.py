import sys

sys.stdin = open("ExpertAcademy4366.txt")

for tc in range(int(input())):
    two = list(input())
    three = list(input())
    an = 0
    for i in range(len(two)):
        temp2 = two.copy()
        temp2[i] = str(abs(int(temp2[i]) - 1))
        tempint2 = int(''.join(temp2), 2)
        print(''.join(temp2), tempint2)
        print("---------")
        for g in range(len(three)):
            temp3 = three.copy()
            temp3[g] = str(abs(int(temp3[g]) - 1))
            tempint3 = int(''.join(temp3), 3)
            print(''.join(temp3), tempint3)

            if tempint2 == tempint3:
                an = tempint2
                break
            temp3[g] = str(abs(int(temp3[g]) - 1))
            tempint3 = int(''.join(temp3), 3)
            print(''.join(temp3), tempint3)

            if tempint2 == tempint3:
                an = tempint2
                break
        print('---------')
        if an:
            break
            # print(i, g)
    print("#{} {}".format(tc + 1, an))
