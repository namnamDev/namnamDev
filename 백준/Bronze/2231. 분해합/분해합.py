a = int(input())
i = 0
an = 0
while i < a:
    t_i = str(i)
    t = 0
    for ii in t_i:
        t += int(ii)
    if i + t == a:
        an = i
        break
    i += 1
if i == a:
    print(0)
else:
    print(i)