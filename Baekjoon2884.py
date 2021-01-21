line = input().split()
H = int(line[0])
M = int(line[1])
Q = 45
bef = M-Q
if bef < 0 :
    bef+=60
    H-=1
if(H<0):
    H+=24

print(f'{H} {bef}')