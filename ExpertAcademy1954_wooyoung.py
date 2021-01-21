T = int(input())
for t in range(T):
    N = int(input())
    if N == 1:
        print(f"#{t+1}\n1")
    else:
        print(f"#{t+1}")
        ans = [[0 for _ in range(N)] for _ in range(N)
        x = 0
        y = 0
        # 방향 - 0 : 오른쪽, 1 : 아래쪽, 2 : 왼쪽, 3 : 위쪽
        direction = 0
        value = 1
        ans[y][x] = value
        while value != N ** 2:
            # 오른쪽
            if direction == 0:
                while 1: 
                    x += 1
                    if x == N or ans[y][x] != 0:
                        x -= 1
                        break
                    value += 1
                    ans[y][x] = value
                direction = 1
            # 아래쪽
            elif direction == 1:
                while 1:
                    y += 1
                    if y == N or ans[y][x] != 0:
                        y -= 1
                        break
                    value += 1
                    ans[y][x] = value
                direction = 2
            # 아래쪽
            elif direction == 2:
                while 1:
                    x -= 1
                    if x == -1 or ans[y][x] != 0:
                        x += 1
                        break
                    value += 1
                    ans[y][x] = value
                direction = 3
            # 아래쪽
            elif direction == 3:
                while 1:
                    y -= 1
                    if y == -1 or ans[y][x] != 0:
                        y += 1
                        break
                    value += 1
                    ans[y][x] = value
                direction = 0
        for y in range(N):
            for x in range(N):
                print(ans[y][x], end=" ")
            print()