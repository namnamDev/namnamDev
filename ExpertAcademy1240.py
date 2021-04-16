import sys

sys.stdin = open('ExpertAcademy1240.txt')

arr = {
    '0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
    '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'
}

for tc in range(int(input())):
    N, M = map(int, input().split())
    line = [input() for _ in range(N)]
    res = []
    x = 0
    y = 0
    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            if line[i][j] == '1':
                x = i
                y = j - 55
                break
        if x != 0:
            break

    for i in range(8):
        res.append(int(arr[line[x][y:y + 7]]))
        y += 7
    num = 0
    for i in range(4):
        num += res[i * 2]
    num *= 3

    for g in range(4):
        num += res[2 * g + 1]
    ans = 0 if num % 10 else sum(res)

    print('#{} {}'.format(tc + 1, ans))
