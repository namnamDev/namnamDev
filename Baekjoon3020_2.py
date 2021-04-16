import sys

sys.stdin = open('Baekjoon3020.txt')
N, M = map(int, input().split())
fly = [0] * M
aa = 0
down = [0] * (M + 1)
up = [0] * (M + 1)
minh = N
count = 0
for i in range(0, N, 2):
    down[int(input())] += 1
    up[int(input())] += 1

for i in range(1, M + 1):
    if minh > (down[i] + up[M - i + 1]):
        minh = (down[i] + up[M - i + 1])
    elif minh == (down[i] + up[M - i + 1]):
        count += 1

print(minh, count)
