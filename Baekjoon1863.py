import sys

sys.stdin = open("Baekjoon1863.txt")
N = int(input())
stack = [0]
cnt = 0
for tc in range(N):
    x, y = map(int, input().split())
    while len(stack) != 0:
        temp = stack[len(stack) - 1]
        if temp < y:
            stack.append(y)
        else:
            if temp > y:
                cnt += 1
                stack.pop()
            if temp == y:
                break

print(cnt + len(stack) - 1)
