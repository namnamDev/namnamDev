import sys

sys.stdin = open("Baekjoon4949.txt")

re = True
while re:
    a = input()
    an = "yes"
    if a == ".":
        re = False
        break
    stack = []
    # print(ord("("), ord(")"), ord("["), ord("]"))
    for i in a:
        if i == "(":
            stack.append(i)
        elif i == "[":
            stack.append(i)
        elif i == ")" or i == "]":
            if not stack:
                an = "no"
                break
            else:
                if i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    an = "no"
                    break
    if stack:
        an = "no"
    print(an)
