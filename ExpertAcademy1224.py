import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy1224.txt")

operator = ["+", "-", "/", "*"]
for tc in range(1, 11):
    N = int(input())
    stack = []
    numStack = []
    M = list(input())
    # print(line)
    sums = 0
    for i in range(N):
        if M[i].isdigit():
            numStack += [int(M[i])]
        elif M[i] == "(":
            stack += ["("]
        elif M[i] == "+" or M[i] == "-":
            stack += [M[i]]
            if len(stack) > 0 and len(numStack) >= 2:
                while True:
                    if stack[-1] == "*" or stack[-1] == "/" or stack[-1] == "(":
                        break
                    oper = stack.pop()
                    print(stack)
                    b = numStack.pop()
                    a = numStack.pop()
                    c = 0
                    if oper == "+":
                        c = a + b
                    elif oper == "-":
                        c = a - b
                    numStack += [c]
                    print(numStack)
            else:
                stack += [M[i]]
        elif M[i] == "*" or M[i] == "/":
            stack += [M[i]]
            # if len(numStack) >= 2:
            #     b = numStack.pop()
            #     a = numStack.pop()
            #     c = 0
            #     if M[i] == "*":
            #         c = a * b
            #     else:
            #         c = a / b
            #     numStack += [c]
        elif M[i] == ")":
            print(stack)
            print(numStack)
            while True:
                oper = stack.pop()
                print(stack)
                if oper == "(":
                    break
                b = numStack.pop()
                a = numStack.pop()
                c = 0
                if oper == "+":
                    c = a + b
                elif oper == "*":
                    c = a * b
                numStack += [c]
                print(numStack)
    print(numStack)
    print("#{} {}".format(tc, numStack[0]))

# 1 672676
# 2 1974171
# 3 12654
# 4 38756
# 5 4035
# 6 155304
# 7 6964
# 8 2819
# 9 24711
# 10 208785
