sums = 0
for i in range(5):
    a = int(input())
    if a < 40 :
        a = 40
    sums += a
print(int(sums/5))