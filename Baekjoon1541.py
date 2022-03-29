import sys

sys.stdin = open("Baekjoon1541.txt")
sen = input()
stack_num = []
stack_oper = []
temp_num = ""
an = 0
check = True
for i in sen:
    if i.isdigit():
        temp_num += i
    else:
        if i == "-":
            stack_oper.append(1)
        else:
            stack_oper.append(0)
        stack_num.append(int(temp_num))
        temp_num = ""
