N, K = map(int, input().split())
li = list(range(1, N + 1))
an = ""
start = 0
temp = list(li)
stack = []
while len(li) > 0:
    Ktemp = K
    print(len(temp), Ktemp)
    if start + Ktemp > len(temp):
        print("hesr")
        Ktemp %= len(li)
        temp += list(li)
    start += Ktemp
    print(temp, start)
    # print(temp[start])
    stack += [li.pop(li.index(temp[start]) - 1)]
    print(stack)
    if len(li) == 0:
        break
print(start)
