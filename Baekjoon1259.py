import sys

sys.stdin = open("Baekjoon1259.txt")

while True:
    N = input()
    if N == '0':
        break
    else:
        a = N[:len(N) // 2]
        b = []
        if len(N) % 2:
            b = N[len(N) // 2 + 1:]
        else:
            b = N[len(N) // 2:]
        tempB = ""
        for i in range(len(b) - 1, -1, -1):
            tempB += b[i]
        if a == tempB:
            print("yes")
        else:
            print("no")
