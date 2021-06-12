import sys

sys.stdin = open('StarDraft 승부 예측하기.txt')


def tour(arr):
    print(arr, len(arr) // 2, len(arr))
    if len(arr) == 2:
        print('tour!')
        if (arr[0][0] == 0 and arr[1][0] == 1) or (arr[0][0] == 1 and arr[0][1] == 2) or (
                arr[0][0] == 2 and arr[0][1] == 0):
            return arr[0]
        else:
            return arr[1]
    elif len(arr) > 2:
        # print(len(arr) // 2, len(arr))
        tour(arr[0:len(arr) // 2])
        tour(arr[len(arr) // 2 + 1:len(arr)])
    return
    # elif arr[0][0] == 1 and arr[0][1] == 2:
    #     return arr[0]


for tc in range(int(input())):
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        arr[i] = [arr[i], i]
    print(arr)
    while len(arr) >= 2:
        temp = len(arr) // 2
        temparr = []
        for i in range(temp):
            fir = arr[i * 2]
            sec = arr[i * 2 + 1]
            print(fir, sec)
            if (fir[0] == 1 and sec[0] == 2) or (fir[0] == 2 and sec[0] == 3) or (
                    fir[0] == 3 and sec[0] == 1) or (fir[0] == sec[0]):
                print('win fir')
                temparr.append(fir)
            else:
                print('win sec')
                temparr.append(sec)
        print(temparr, len(temparr))
        arr = temparr
    print("#{} {}".format(tc + 1, arr[0][1]))
