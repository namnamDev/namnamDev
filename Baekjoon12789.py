import sys

sys.stdin = open('Baekjoon12789.txt')
from collections import deque

N = int(input())

my_d = list(map(int, input().split()))

visit = [0] * len(my_d)
number = 1
for i in range(len(my_d)):
    if my_d[i] == number:
        number += 1
        visit[i] = 1
print(number)
for i in range(len(my_d) - 1, -1, -1):
    print(my_d[i])
    if my_d[i] == number:
        number += 1
        visit[i] = 1

print (visit)
if visit.count(0):
    print("Sad")
else:
    print("Nice")