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
            if len(stack) > 0:
                if stack.pop() == "*":
                    numStack += [numStack.pop() * numStack.pop()]
                # else:
                #     sums = 0
                #     for g in range(len(numStack)):
                #         if len(stack) > 0:
                #             if stack.pop() == "+":
                #                 sums += numStack.pop()
                #             else:
                #                 break
                #         else:
                #             break
                #     numStack += [sums]

        else:
            stack += [chr(num + ord("0"))]
    # if stack:
    #     numStack += stack
    # print(sum(numStack))
    print("#{} {}".format(tc, sum(numStack)))
