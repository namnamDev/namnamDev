import sys
T = int(sys.stdin.readline())
for i in range(T):
    lines = sys.stdin.readline().rstrip().split()
    print(int(lines[0])+int(lines[1]))
