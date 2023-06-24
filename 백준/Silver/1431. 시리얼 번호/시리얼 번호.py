def my_function(A, B):
    if len(A) < len(B):
        return A, B
    elif len(B) < len(A):
        return B, A

    size = len(A)
    sumA = sumB = 0
    for idx in range(size):
        if 48 <= ord(A[idx]) <= 57:
            sumA += int(A[idx])
        if 48 <= ord(B[idx]) <= 57:
            sumB += int(B[idx])
    if (sumA < sumB):
        return A, B
    elif (sumB < sumA):
        return B, A
    arr = [A, B]
    return sorted(arr)


word_list = [input() for _ in range(int(input()))]

for a in range(len(word_list)):
    for b in range(a + 1, len(word_list)):
        res = my_function(word_list[a], word_list[b])
        word_list[a], word_list[b] = res[0], res[1]

print(*word_list, sep='\n')