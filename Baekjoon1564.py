import sys

sys.stdin = open('Baekjoon1564.txt')


N = int(input())
a = 100000
t = 1
while N > 0:
    # t *= (N % a)
    t *= N
    while not t % 10:
        t //= 10
    t %= a
    N -= 1
answer = str(t)
while len(answer) < 5:
    answer = "0"+answer
print(answer)
