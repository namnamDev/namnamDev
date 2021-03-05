import sys

sys.stdin = open("Baekjoon1302.txt")

T = int(input())
book = {}
for tc in range(T):
    name = input()
    book[name] = book.get(name, 0) + 1
maxSale = 0
maxSaleIdx = 0
for i in book:
    if book[i] > maxSale:
        maxSale = book[i]
        maxSaleIdx = i
    elif book[i] == maxSale:
        tempLen = len(book[i])
        maxLen = len(book[maxSaleIdx])

        for f in range(len(book[i])):

print(book[maxSaleIdx])
