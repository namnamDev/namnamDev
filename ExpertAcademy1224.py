import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy1224.txt")

for tc in range(1, 11):
    N = int(input())
    stack = []
    numStack = []
    line = list(input())
    # print(line)
    sums = 0
    for i in range(N):
        num = ord(line[i]) - ord("0")

        if num >= 0:
            numStack += [num]
        elif line[i] == "*":
            if len(stack) > 0:
                while stack[-1] != "*":
                    numStack += [stack.pop()]
                    if (len(stack)) == 0:
                        break
            stack += ["*"]
        else:
            g = 0
            if len(stack) > 0:
                while stack[-1] != "+":
                    numStack += [stack.pop()]

                    if (len(stack)) == 0:
                        break
            stack += ["+"]
    if stack:
        numStack += stack
    print(numStack)
    # print("#{} {}".format(tc))
