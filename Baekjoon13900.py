T = int(input())
a = list(map(int , input().split()))
s = sum(a)
u =0
for i in a:
    s -= i
    u += i*s
print(u)