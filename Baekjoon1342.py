import sys

sys.stdin = open("Baekjoon1342.txt")


def dfs(N):
    global temp
    global an
    if N == n:
        print(an)
        return
    else:
        a = 0
        while a < 26:
            if temp[a]:
                temp[a] -= 1
                an.append(chr(a + 97))
                dfs(N + 1)
            else:
                a += 1


S = input()
n = len(S)
temp = [0] * 26
an = []
print(ord('a'), ord('z'), ord('z') - ord('a'))
for i in S:
    temp[ord(i) - 97] += 1

print(temp)
dfs(0)
# setS = set(S)
# print(setS)
# for i in setS:
#     temp = [i]
#     dfs(1)
