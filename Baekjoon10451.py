import sys

sys.stdin = open('Baekjoon10451.txt')

for _ in range(int(input())):
    a = int(input())
    arr = list(map(int, input().split()))
    an = 0
    vi = [0] * a
    aas = []
    for i in range(a):
        if not vi[i]:
            temp = [i]
            vi[i] = 1
            Q = [arr[i]]
            while Q:
                n = Q.pop()
                if not vi[n - 1]:
                    vi[n - 1] = 1
                    Q.append(arr[n - 1])
                    temp.append(arr[n - 1])
            if len(temp):
                aas.append(temp)
    print(len(aas))
