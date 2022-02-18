import sys

sys.stdin = open('Baekjoon2251.txt')


def ch(paArr):
    if not paArr[0]:
        an.append(paArr[2])
    for i in range(3):
        temp = []
        if paArr[i]:
            fir = (i + 1) % 3
            sec = (i + 2) % 3
            if paArr[fir] < arr[fir]:
                if paArr[fir] + paArr[i]<= arr[fir]:
                    ch()
                elif paArr[fir] + paArr[i]> arr[fir]:
            if paArr[sec] < arr[sec]:
                paArr
    # if a < A:
    #     if A < a + b:
    #         ch(A, b - a, c)
    #     elif A > a + b:
    #         ch(a + b, 0, c)
    # if b<B:


an = []
vi = []
arr = list(map(int, input().split()))
