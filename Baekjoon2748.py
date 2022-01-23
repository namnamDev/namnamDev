a = int(input())
aa = [0, 1, 1]
while len(aa) <= a:
    aa.append(aa[-1] + aa[-2])
print(aa[-1])
