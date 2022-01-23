a = int(input())
A = [1, 0]
B = [0, 1]
while len(A) <= a:
    A.append(A[-1] + A[-2])
    B.append(B[-1] + B[-2])
print(A[a], B[a])
# A --- 0  1 0
# B --- 1  0 1
# BA -- 2  1 1
# BAB -- 3 1 2
# BABBA--4 2 3
