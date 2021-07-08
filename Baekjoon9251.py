import sys

sys.stdin = open('Baekjoon9251.txt')
A = list(input())
B = list(input())
max_cnt = 0
a = 0
viA = [0] * len(A)
viB = [0] * len(B)
while a < len(A):
    an = ''
    cnt = 0
    b = 0
    for i in range(len(A)):
        if not viA[i]:
            viA[i] = 1
    # for i in range(a, len(A)):
    #     tempA = A[i]
    #     for g in range(b, len(B)):
    #         tempB = B[g]
    #         if tempB == tempA:
    #             cnt += 1
    #             an += tempB
    #             b = g + 1
    #             break
    max_cnt = max(cnt, max_cnt)
    print(an, len(an))
    a += 1
print(max_cnt)
# while b <= len(B):
#     tempB = B[b]
#     if tempA == tempB:
#         break
#     b += 1
# for g in range(len(B)):
#     tempB = B[g]
