import sys

sys.stdin = open('Baekjoon1213.txt')
a = list(input())
an = ""
tAn = ""
tmid = ""
vi = [0] * 26
for i in a:
    vi[ord(i) - 65] += 1
aBool = True
for ii in range(26):
    tA = vi[ii]
    an += chr(ii + 65) * (tA // 2)
    tAn = chr(ii + 65) * (tA // 2) + tAn
    if tA % 2:
        if not tmid:
            tmid = chr(ii + 65)
        else:
            aBool = False
            break
if aBool:
    print(an + tmid + tAn)
else:
    print("I'm Sorry Hansoo")
# if vi.count(1) > 1:
#     an = "I'm Sorry Hansoo"
# else:
#     while
# # print(vi)
