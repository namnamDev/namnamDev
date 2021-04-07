import sys

sys.stdin = open('ExpertAcademy1233.txt')


def check_tree(num):
    global an
    if not an:
        return
    if num:
        left = arr[num][1]
        right = arr[num][2]
        if not arr[num][0]:  # 부호일때
            if check_tree(left) and check_tree(right):  # 좌우 하나라도 비어있으면 false
                an = 0
                return
        else:  # 숫자일때
            if check_tree(left) or check_tree(right):  # 둘중 하나라도 있으면
                an = 0
                return
        return True


for tc in range(10):
    N = int(input())
    arr = [[0] * 3 for _ in range(N + 1)]
    an = 1
    for i in range(N):
        temp = list(input().split())
        while len(temp) < 4:
            temp.append('0')
        position = int(temp[0])
        if temp[1] == '-' or temp[1] == '+' or temp[1] == '*' or temp[1] == '/':
            arr[position][0] = False
        else:
            arr[position][0] = True
        arr[position][1] = int(temp[2])
        arr[position][2] = int(temp[3])
    check_tree(1)
    print('#{} {}'.format(tc + 1, an))
