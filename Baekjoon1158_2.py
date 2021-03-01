N, K = map(int, input().split())
li = list(range(1, N + 1))
an = ""
start = 0
temp = list(li)
stack = []
while len(li) > 0:
    Ktemp = K
    if start + Ktemp > len(temp):
        Ktemp %= len(li)
        if not Ktemp:
            Ktemp += len(li)
        temp += list(li)
    start += Ktemp
    stack += [li.pop(li.index(temp[start - 1]))]

    if len(li) == 0:
        break

print("<", end="")
for i in range(N):
    if i != N - 1:
        print("{},".format(stack[i]), end=" ")
    else:
        print("{}>".format(stack[i]))
# an = "<"
# for i in range(N - 1):
#     an += str(stack[i]) + ", "
#
# an += str(stack[N - 1]) + ">"
# print(an)
