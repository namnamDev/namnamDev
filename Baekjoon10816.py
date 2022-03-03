import sys

sys.stdin = open("Baekjoon10816.txt")
N = int(input())
N_arr = list(map(int, input().split()))
M = int(input())
M_arr = list(map(int, input().split()))
M_dic = {}
for i in M_arr:
    M_dic[i] = 1
for ii in N_arr:
    if M_dic.get(ii):
        M_dic[ii] += 1
an_arr = []
for i in M_arr:
    an_arr.append(M_dic[i] - 1)
print(*an_arr)
