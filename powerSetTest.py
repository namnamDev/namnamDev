import sys

sys.stdin = open("powerset.txt")


def powerset(idx):
    global score
    # print(sel)
    tempArr = []
    for i in range(n):
        if sel[i]:
            tempArr.append(arr[i])
    print(tempArr)
    if idx == n:
        return
    # idx 자리의 원소를 뽑고 간다.
    sel[idx] = 1
    powerset(idx + 1)
    # idx 자리의 원소를 안뽑고 간다.
    sel[idx] = 0
    powerset(idx + 1)


arr = list(map(int, input().split()))
n = len(arr)
sel = [0] * n
print(arr)
powerset(0)
