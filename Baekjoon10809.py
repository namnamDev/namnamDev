S = input()
alpabet = [-1]*26
cnt = 0
for i in S:
    a = ord(i)-97
    if alpabet[a] == -1:
        alpabet[a] = cnt
    cnt+=1

print(*alpabet)