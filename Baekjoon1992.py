import sys
from collections import deque

sys.stdin = open("Baekjoon1992.txt")


def quad(arr, nums):
    Q.append("(")
    if nums == 1:
        Q.append(board[arr[0]][arr[1]])
    else:
        temp = arr[0][0]
        for i in range(nums // 2):
            for g in range(nums // 2):
                if temp != arr[i][g]:
                    quad(arr, nums // 2)
                    break

        Q.append(temp)
        Q.append(")")

        temp2 = arr[0][nums // 2]
        for i in range(nums // 2):
            for g in range(nums // 2, nums):
                if temp2 != arr[i][g]:
                    quad(arr, nums // 2)
                    break
        Q.append(temp2)
        Q.append(")")
        temp3 = arr[nums // 2][0]
        for i in range(nums // 2, nums):
            for g in range(nums // 2):
                if temp3 != arr[i][g]:
                    quad(arr, nums // 2)
                    break
        Q.append(temp3)
        Q.append(")")
        temp4 = arr[nums // 2][nums // 2]
        for i in range(nums // 2, nums):
            for g in range(nums // 2, nums):
                if temp4 != arr[i][g]:
                    quad(arr, nums // 2)
                    break
        Q.append(temp4)
        Q.append(")")


T = int(input())
board = [list(map(int, input())) for _ in range(T)]
for i in board:
    print(i)
Q = []
quad(board, T)

print(*Q)
