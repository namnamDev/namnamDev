s = input()
stack = []
stack2 = ""
answer = ""
for i in s:
    if i == '<':
        stack.append(i)
        temp_arr = stack2.split(" ")
        for temp_idx in range(len(temp_arr)):
            temp_arr[temp_idx] = temp_arr[temp_idx][::-1]
        answer += " ".join(temp_arr)
        stack2 = ""
    elif i == '>':
        stack.append(i)
        answer += "".join(stack)
        stack = []
    elif stack:
        stack.append(i)
    elif not stack:
        stack2 += i

if stack2:
    temp_arr = stack2.split(" ")
    for temp_idx in range(len(temp_arr)):
        temp_arr[temp_idx] = temp_arr[temp_idx][::-1]
    answer += " ".join(temp_arr)

print(answer)