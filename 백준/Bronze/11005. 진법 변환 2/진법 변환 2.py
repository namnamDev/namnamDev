N, B = map(int, input().split())
t = N
an = ""
arr = []
for i in range(10):
    arr.append(str(i))
for i in range(26):
    arr.append(chr(65 + i))
while t:
    an = arr[t % B] +an
    t //= B
print(an)