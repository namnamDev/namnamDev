import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy1224.txt")

for tc in range(1, 11):
    N = int(input())
    Data = input()
    stack = []
    num_lst = []

    icp = {'*': 2, '+': 1, '(': 3}  # 넣을때
    isp = {'*': 2, '+': 1, '(': 0}  # 스택안

    # Step 1: 중위 => 후위 표기법 변경
    for i in range(N):
        # 피연산자인 경우: 숫자 리스트 넣기
        if Data[i].isdigit():
            num_lst.append(Data[i])

        # 연산자인 경우
        else:
            # stack이 빈 경우 => 무조건 append(여는 괄호의 case)
            if not stack:
                stack.append(Data[i])
                continue

            # stack이 비지 않은 경우
            elif stack:
                # 닫는 괄호인 경우, 여는 괄호가 나올 때 까지 pop
                if Data[i] == ')':
                    while stack[-1] != '(':
                        num_lst.append(stack.pop())
                    stack.pop()

                # icp & isp 비교
                elif icp[Data[i]] > isp[stack[-1]]:
                    stack.append(Data[i])

                else:
                    # icp가 isp 보다 작으면 계속 pop & 연산자 리스트에 append
                    while icp[Data[i]] <= isp[stack[-1]]:
                        num_lst.append(stack.pop())
                    stack.append(Data[i])

    # print(num_lst)

    # step 2: 계산
    for i in range(len(num_lst)):
        if num_lst[i].isdigit():
            stack.append(num_lst[i])

        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())

            if num_lst[i] == "+":
                result = num1 + num2
            elif num_lst[i] == "*":
                result = num1 * num2

            stack.append(str(result))

    print('#{} {}'.format(tc, stack[0]))

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
