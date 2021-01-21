NX = input().split()
N = int(NX[0])
X = int(NX[1])
line = input().split()
answer = ''
for i in line:
    if int(i)<X:
        answer += f'{i} '

print(answer)
