import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy1248.txt")


# 1 3 8
# 2 1 10


def do_tree(num):
    arr = []
    if num:
        if num not in arrM:
            arr.append(num)
            arrM.append(num)
            arr += do_tree(tree[num][0])
        else:
            global an
            an = num
            arr.append(num)
    return arr


def cnt_tree(num):
    if num:
        global cnt
        cnt += 1
        cnt_tree(tree[num][1])
        cnt_tree(tree[num][2])


for tc in range(int(input())):
    V, E, N1, N2 = map(int, input().split())
    lines = list(map(int, input().split()))
    # print(V, E, N1, N2)
    # print(lines)
    tree = [[0] * 3 for _ in range(V + 1)]
    for i in range(0, (E) * 2, 2):
        mother, child = lines[i], lines[i + 1]

        if not tree[mother][1]:
            tree[mother][1] = child
        else:
            tree[mother][2] = child
        tree[child][0] = mother
    arrM = []
    an = 0
    cnt = 0
    arr1 = do_tree(N1)
    arr2 = do_tree(N2)
    cnt_tree(an)
    print('#{} {} {}'.format(tc + 1, an, cnt))
