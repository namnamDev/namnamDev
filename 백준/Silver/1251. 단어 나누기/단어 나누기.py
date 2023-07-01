string = input()
arr = list(string)
size = len(arr)
answer = "".join(arr[:1][::-1]) + "".join(arr[1:2][::-1]) + "".join(arr[2:][::-1])
for fir in range(1, size - 1):
    for sec in range(fir + 1, size):
        word = "".join(arr[:fir][::-1]) + "".join(arr[fir:sec][::-1]) + "".join(arr[sec:][::-1])
        answer = sorted([answer, word])[0]

print(answer)