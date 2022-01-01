import sys

sys.stdin = open('Baekjoon1475.txt')
N = input()
vi = [0] * 10
for i in N:
    vi[int(i)] += 1
temp = (vi[6] + vi[9]) // 2
if (vi[6] + vi[9]) % 2:
    temp += 1
vi[6] = vi[9] = temp

print(max(vi))
