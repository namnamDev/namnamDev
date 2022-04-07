a = list(input())
stack = []
stack2 = []
check = True
for i in a:
    if i == ")" or i == "]":
        if not stack:
            check = False
            break

        if i == ")" and stack[-1][0] == "(":
            stack2.append([2, stack[-1][1]])
            stack.pop()

        elif i == "]" and stack[-1][0] == "[":
            stack2.append([3, stack[-1][1]])
            stack.pop()
        else:
            check = False
            break
    else:
        if stack:
            stack.append([i, stack[-1][1] + 1])
        else:
            stack.append([i, 0])
if stack:
    check = False
if check:
    i = 0
    while len(stack2) > 1:
        t = stack2[i]
        aa = 1
        r = i - 1
        while r >= 0:
            if stack2[r][1] < stack2[i][1]:
                break
            elif stack2[r][1] == stack2[i][1]:
                stack2[r][0] += stack2[i][0]
                stack2.pop(i)
                i -= 1
            else:
                stack2[r][0] *= stack2[i][0]
                stack2[r][1] -= 1
                stack2.pop(i)
                i -= 1
            r -= 1
        i += 1
    print(stack2[0][0])
else:
    print(0)
