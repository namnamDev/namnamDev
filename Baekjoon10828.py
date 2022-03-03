import sys

sys.stdin = open("Baekjoon10828.txt")
N = int(sys.stdin.readline())
stack = []
for n in range(N):
    a = sys.stdin.readline().split()
    t = a[0]
    if t == "push":
        stack.append(a[1])
    elif t == "pop":
        print(stack.pop() if len(stack) else -1)
    elif t == "size":
        print(len(stack))
    elif t == "empty":
        print(0 if len(stack) else 1)
    elif t == "top":
        print(stack[-1] if len(stack) else -1)
