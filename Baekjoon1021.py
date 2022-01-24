import sys

sys.stdin = open("Baekjoon1021.txt")

from collections import deque


def pick(numsIdx, cnt, paArr):
    if numsIdx == M:
        print(cnt)
        return
    temp = paArr + paArr
    lenPaArr = len(paArr)
    for i in range(lenPaArr):
        if paArr[i] == nums[numsIdx]:
            tempArr = temp[i + 1:i + lenPaArr]
            # print("R", i, nums[numsIdx], tempArr)
            pick(numsIdx + 1, cnt + i, tempArr)
            break
        if paArr[lenPaArr - 1 - i] == nums[numsIdx]:
            tempArr = temp[lenPaArr - i:-i - 1]
            pick(numsIdx + 1, cnt + i + 1, tempArr)
            break


N, M = map(int, input().split())
nums = list(map(int, input().split()))
arr = list(range(1, N + 1))
pick(0, 0, arr)
