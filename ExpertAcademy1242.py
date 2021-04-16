import sys

sys.stdin = open('ExpertAcademy1242.txt')

arr = {
    '3211': '0', '2221': '1', '2122': '2', '1411': '3', '1132': '4',
    '1231': '5', '1114': '6', '1312': '7', '1213': '8', '3112': '9'
}

for tc in range(int(input())):
    N, M = map(int, input().split())
    line = [input() for _ in range(N)]
    res = []
    x = 0
    y = 0
    temp_arr = ''
    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            if line[i][j] != '0':
                x = i
                temp_arr = line[i][j] + temp_arr
        if x != 0:
            print(temp_arr)
            break
    # pwsize = 7
    # for i in range(8):
    #     res.append(int(arr[line[x][y:y + 7]]))
    #     y += 7
    # num = 0
    # for i in range(4):
    #     num += res[i * 2]
    # num *= 3
    #
    # for g in range(4):
    #     num += res[2 * g + 1]
    # ans = 0 if num % 10 else sum(res)

    # print('#{} {}'.format(tc + 1, ans))
