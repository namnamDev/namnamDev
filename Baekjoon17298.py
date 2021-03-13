import sys

sys.stdin = open("Baekjoon17298.txt")


def NGE(nums):
    global answer
    an = -1
    for i in range(nums, N):
        if arr[nums] < arr[i]:
            an = arr[i]
            break
    answer += str(an)


N = int(input())
arr = list(map(int, input().split()))
print(N, arr)
answer = ""

for i in range(N):
    NGE(i)
