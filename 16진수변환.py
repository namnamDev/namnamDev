sample = '1DB176C588D26EC'
for i in range(len(sample) - 1, -1, -1):
    temp = sample[i]
    a = '0000'

    # int(sample, 16)
print(bin(int('1DB176C588D26EC', 16)))
print(int(sample, 16))

a = int(sample, 16)
temp = ""
while a:
    temp = str(a % 2) + temp
    a //= 2
print(temp)
