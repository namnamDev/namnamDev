import sys

sys.stdin = open("Baekjoon1593.txt")

N, M = map(int, input().split())
Nw, Mw = list(input()), list(input())
cnt = 0
print(cnt)
for i in range(2 ** M):
    if M & i:
        print(i)
#
# for n in range(N):
#     if ord(Nw[n]) > 90:
#         Nw[n] = chr(ord(Nw[n]) - 32)
#     if ord(Mw[m + n]) > 90:
#         Mw[m + n] = chr(ord(Mw[m + n]) - 32)
#     print(m, n, Mw[m + n], Nw[n])
#     if Mw[m + n] != Nw[n]:
#         break
#     if n == N - 1:
#         cnt += 1
# n = m = 0
print(cnt)
# while m < M:
#     if ord(Mw[m]) > 90:
#         Mw[m] = chr(ord(Mw[m]) - 32)
#     while n < N:
#         if ord(Nw[n]) > 90:
#             Nw[n] = chr(ord(Nw[n]) - 32)
#         if N[n] == M[m]:
#             n += 1
#             m += 1
#         else:
