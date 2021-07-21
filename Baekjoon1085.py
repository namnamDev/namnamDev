import sys

sys.stdin = open('Baekjoon1085.txt')
x, y, w, h = map(int, input().split())
an = min(x, y, w - x, h - y)
print(an)
