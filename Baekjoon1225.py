import sys

sys.stdin = open("Baekjoon1225.txt")

# a, b = input().split()
# an = 0
# for i in a:
#     for ii in b:
#         an += int(i) * int(ii)
# print(an)
a, b = map(eval, map('+'.join, input().split()));
print(a, b)
