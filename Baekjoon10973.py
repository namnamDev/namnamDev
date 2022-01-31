import sys

sys.stdin = open('Baekjoon10973.txt')

# def ch(pa):
#     if len(pa) == t:
#         global arr
#         if pa == ar:
#             print(arr)
#         arr = []
#         for i in pa:
#             arr.append(i)
#         return
#     for i in range(1, t + 1):
#         if not vi[i]:
#             vi[i] = 1
#             ch(pa + [i])
#             vi[i] = 0


t = int(input())
ar = list(map(int, input().split()))
an = -1
for a in range(t):
    vi = [0] * (t + 1)
    arr = [a]
    vi[a] = 1
    while arr:
        no = arr.pop()
        if len(arr) == t:
            print(arr)
        for i in range(1, t + 1):
            if not vi[i]:
                vi[i] = 1
                arr.append(i)
                vi[i] = 0
