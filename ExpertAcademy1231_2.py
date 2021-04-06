import sys

sys.stdin = open('ExpertAcademy1231.txt')


def in_order(node):
    global answer
    if node:
        in_order(arr[node][0])
        answer += arr[node][2]
        in_order(arr[node][1])


for tc in range(10):
    answer = ''
    N = int(input())
    arr = [[0] * 3 for _ in range(N + 1)]
    for i in range(N):
        line = list(input().split())
        while len(line) < 4:
            line.append('0')
        my, word, left, right = map(str, line)
        arr[int(my)][0] = int(left)
        arr[int(my)][1] = int(right)
        arr[int(my)][2] = word
    in_order(1)
    print("#{} {}".format(tc + 1, answer))
