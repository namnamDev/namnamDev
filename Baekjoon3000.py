import sys

sys.stdin = open("Baekjoon3000.txt")


def geli(d1, d2):
    d1 = arr[d1]
    d2 = arr[d2]
    return ((d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2) ** 0.5


def pita(aa, bb, cc):
    aa = int(aa ** 2)
    bb = int(bb ** 2)
    cc = int(cc ** 2)

    # print(aa ** 2, bb ** 2, cc ** 2)
    # print(cc ** 2 == aa ** 2 + bb ** 2)
    # print(aa ** 2 == bb ** 2 + cc ** 2)
    # print(bb ** 2 == aa ** 2 + cc ** 2)
    if (cc == aa + bb) or (aa == bb + cc) or (bb == aa + cc):
        return True
    else:
        return False


def py(aa, bb, cc):
    if aa[0] == bb[0] or aa[0] == cc[0] or bb[0] == cc[0] or aa[1] == bb[1] or aa[1] == cc[1] or bb[1] == cc[1]:
        return True


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)
cnt = 0
for i in range(N - 2):
    for g in range(i + 1, N - 1):
        a = geli(i, g)
        for f in range(g + 1, N):
            b = geli(g, f)
            c = geli(i, f)
            print(i, g, f, a, b, c)
            print(pita(a, b, c), py(arr[i], arr[g], arr[f]))
            if pita(a, b, c) and py(arr[i], arr[g], arr[f]):
                print(i, g, f)
                cnt += 1
print(cnt)
