n = input()
lenN = len(n)
print(lenN)
for i in range(len(n)):
    for g in range(i, len(n)):
        print(i, g)
        temp = n[g]
        if temp == n[i]:
            n = n.replace(temp, "")
            n = n.replace(temp, "")
            print(n)

print(n)
