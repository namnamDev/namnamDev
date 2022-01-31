import sys

sys.stdin = open("Baekjoon17253.txt")
a = int(input())
an = "YES"
while a > 0:
    if a % 3 == 2:
        an = "NO"
        break
    a //= 3
print(an)
for i in range(299):
    s = i
    ann = "YES"
    ss = ""
    while i > 0:
        if i % 3 == 2:
            ann = "NO"
            # break
        ss = str(i % 3) + ss
        i //= 3
    print(s, ann, ss)
