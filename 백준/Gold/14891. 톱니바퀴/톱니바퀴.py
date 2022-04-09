def turn(pdr, pidx):
    parr = arr[pidx]
    if pdr == 1:  # 시계방향
        t = parr.pop()
        temp = [t] + parr
    else:
        t = parr.pop(0)
        temp = parr + [t]
    return temp


arr = [list(input()) for _ in range(4)]
K = int(input())
dr = [list(map(int, input().split())) for _ in range(K)]
for s, d in dr:
    s -= 1
    wl = wr = s
    wld = wrd = d
    turn_list = [[d, s]]
    while 1 <= wl and arr[wl][6] != arr[wl - 1][2]:
        wld *= -1
        turn_list.append([wld, wl - 1])
        wl -= 1
    while wr < 3 and arr[wr][2] != arr[wr + 1][6]:
        wrd *= -1
        turn_list.append([wrd, wr + 1])
        wr += 1
    for dr, idx in turn_list:
        arr[idx] = turn(dr, idx)
an = 0
for one in range(4):
    if arr[one][0] == "1":
        an += 2 ** one
print(an)