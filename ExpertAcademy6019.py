import sys

sys.stdin = open("ExpertAcademy6019.txt")
T = int(input())
for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    start, fly, s = 0, 0, 0
    end = D
    while start != end:
        print(start, end, "-----")
        if fly == start:
            temp = 0
            while temp <= end:
                print(start, end, temp, s)
                start += A * s
                end -= B * s
                temp += F * s
                s += 1
                if temp >= end:
                    break
            fly = end
        if fly == end:
            temp = end
            while temp <= start:
                print(start, end, temp, s)
                start += A * s
                end -= B * s
                temp -= F * s
                s += 1
                if temp <= start:
                    break
            fly = start
        if end <= start:
            break
    print(s)
