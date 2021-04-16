import sys

sys.stdin = open('ExpertAcademy11767.txt')

for tc in range(int(input())):
    arr = list(map(int, input().split()))
    dp2 = [0] * 10
    dp1 = dp2.copy()
    an = 0
    for i in range(12):
        t = arr[i]
        if not i % 2:
            dp1[t] += 1
            minidx = 0 if t - 2 < 0 else t - 2
            triplet = dp1[minidx:t + 3]
            # print('tri1', t, minidx, t + 3, triplet)
            runs = 0
            tree = False
            for g in triplet:
                if g:
                    if g == 3:
                        an = 1
                        tree = True
                        break
                    else:
                        runs += 1
                else:
                    runs = 0

                if runs == 3:
                    an = 1
                    break
            if an:
                break
        else:
            dp2[t] += 1
            minidx = 0 if t - 2 < 0 else t - 2
            triplet = dp2[minidx:t + 3]
            # print('tri2', t, minidx, t + 3, triplet)
            runs = 0
            tree = False
            for g in triplet:
                if g:
                    if g == 3:
                        an = 2
                        tree = True
                        break
                    else:
                        runs += 1
                else:
                    runs = 0

                if runs == 3:
                    an = 2
                    break
            if an:
                break

    print("#{} {}".format(tc + 1, an))
