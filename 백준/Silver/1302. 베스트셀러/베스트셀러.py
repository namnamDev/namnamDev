T = int(input())
book = {}
maxCnt = 0
for tc in range(T):
    name = input()
    book[name] = book.get(name, 0) + 1
    maxCnt = max(maxCnt, book[name])
an = []
for i in book:
    if book[i] == maxCnt:
        an.append(i)
print(sorted(an)[0])