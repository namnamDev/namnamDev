import sys
ABC = sys.stdin.readline().split()
A = int(ABC[0])
B = int(ABC[1])
C = int(ABC[2])
answer = -1
if C < B:
    return answer
else:
#(C-B)*N > A+B*N 지점
#C*N -B*N -B*N > A
# (C-2*B)*N>A
# N > A/(C-2*B)
