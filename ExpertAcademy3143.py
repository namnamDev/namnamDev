import sys
sys.stdin = open("ExpertAcademy3143.txt")
T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    lenA = len(A)
    lenB = len(B)
    # print(A,B)
    cnt = 0
    a = 0
    while a < lenA -lenB+1:
        for b in range(lenB):
            if A[a+b] != B[b]:
                # print(A[a + b], B[b])
                a += 1
                break
            if b == lenB-1:
                cnt += 1
                a += lenB
    an = lenA - lenB*cnt + cnt
    print("#{} {}".format(tc, an))




