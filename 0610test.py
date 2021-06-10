board = []
inputs = ['_###_', '_____', '_#_#_', '##A#B']
for i in range(4):
    board.append(list(inputs[i]))
start = []
end = []
for i in range(len(board)):
    for g in range(len(board[i])):
        if board[i][g] == 'A':
            start = [i, g]
        elif board[i][g] == 'B':
            end = [i, g]
vi = [[0] * len(board) for _ in range(len(board[0]))]
print(start, end)
