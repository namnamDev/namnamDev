import sys

sys.stdin = open("Baekjoon6603.txt")


def lec(parr, idx):
    if len(parr) == 6:
        print(*parr)
        return
    for i in range(idx, size):
        lec(parr + [arr[i]], i + 1)


while True:
    arr = list(map(int, input().split()))
    if not arr[0]:
        break
    size = arr.pop(0)
    lec([], 0)
    print()
