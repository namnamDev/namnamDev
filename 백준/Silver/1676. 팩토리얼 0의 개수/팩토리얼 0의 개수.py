num = int(input())
answer = 0
total_2, total_5 = 0, 0
for i in range(num + 1):
    temp_2, temp_5 = i, i
    while temp_2:
        if not temp_2 % 2:
            temp_2 //= 2
            total_2 += 1
        else:
            break
    while temp_5:
        if not temp_5 % 5:
            temp_5 //= 5
            total_5 += 1
        else:
            break
print(min(total_2, total_5))