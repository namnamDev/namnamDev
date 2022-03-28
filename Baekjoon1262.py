import sys

sys.stdin = open('Baekjoon1262.txt')
N, y1, x1, y2, x2 = map(int, input().split())
top = N
for i in range(1, N):
    top = N - i
    an = "." * (N - i)
    t = chr(top % 26 + 97)
    top -= 1
    while len(t) < top - 1:
        t = chr(top % 26 + 97) + t + chr(top % 26 + 97)
        # print(chr(top % 26 + 97))
        top -= 1
    an += t
    an += "." * (N - i)
    print(an)
print(ord("a"), ord("z"))
