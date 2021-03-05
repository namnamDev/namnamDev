import sys

A, B, C = map(int, sys.stdin.readline().split())
if B % 2:
    print(((A ** (B // 2)) ** 2 * A) % C)
else:
    print(((A ** (B // 2)) ** 2) % C)

# print(((abs(A - C)) ** B) % C)
