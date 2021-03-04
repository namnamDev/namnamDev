A, B, C = map(int, input().split())
# print((A ** B) % C)
print(((abs(A - C)) ** B) % C)
