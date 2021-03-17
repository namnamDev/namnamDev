N = input()
an = ''
res = {}
for i in N:
    f = ord(i)
    if (f >= 97):
        f -= 32
    an += chr(f)
ann = set(an)
ms = 0
for i in ann:
    temp = an.count(i)
    an = an.replace(i, '')
    res[temp] = res.get(temp, []) + [i]
    if ms < temp:
        ms = temp

if len(res[ms]) > 1:
    print('?')
else:
    print(*res[ms])
