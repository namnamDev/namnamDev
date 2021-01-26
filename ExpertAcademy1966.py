T = int(input())
for i in range(1,T+1):
    N = int(input())
    line = list(map(int, input().split()))
    line.sort()
    result = '#'+str(i)+' '
    for f in line :
        result += str(f) + ' '
    print(result)