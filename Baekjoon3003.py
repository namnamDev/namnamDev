a, b = map(int, input().split())
an = 0
while an < 1000000:
    temp = an / a
    if temp != an // a:
        temp = an // a + 1

    if temp == b:
        break
    an += 1
print(an)
