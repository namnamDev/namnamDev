N = int(input())
boards = []
result = []
for i in range(N):
    lines = list(map(int , input().split()))
    boards.append(lines)
fir_boards = []

for first_line in range(N):
    temp = []
    for g in range(N):
        temp.append(boards[N-g-1][N-1-first_line])
    fir_boards.append(temp)
sec_boards = []

for sec_line in range(N):
    temp = []
    for g in range(N):
        temp.append(boards[N-1-sec_line][N-g-1])
    sec_boards.append(temp)
thir_boards = []
for thir_line in range(N):
    temp = []
    for g in range(N):
        temp.append(boards[g][N-1-thir_line])
    thir_boards.append(temp)
for i in range(N) :
    print(fir_boards[i] , sec_boards[i] , thir_boards[i])