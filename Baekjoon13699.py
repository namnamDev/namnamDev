import sys

sys.stdin = open("Baekjoon13699.txt")
def my_lec(idx,p_arr):
    if idx <= 1:
        return 1
    if p_arr[idx] != 0:
        return p_arr[idx]

    t = 0
    for i in range(idx):
        t += my_lec(i, p_arr) * my_lec(idx - i - 1, p_arr)

    p_arr[idx] = t

    return p_arr[idx]

n = int(input())

arr = [0]*(n+1)
arr[0] = 1
if n>=1:
    arr[1] = 1
my_lec(n, arr)
print(arr[-1])