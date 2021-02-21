N = input()
lenN = len(N)
max_sums = 0
for fir in range(lenN):
    temp = 1
    temp2 = 0
    for end in range(lenN - 1, fir, -1):
        if N[fir] != N[end]:
            temp += 1
            # print(N[fir], N[end])
        else:
            temp2 += 1

        if temp2 == lenN - fir:
            # print(N[fir], N[end])
            break

    if max_sums < temp:
        # print(max_sums, temp)
        max_sums = temp
if max_sums == 1:
    max_sums = -1

print(max_sums)