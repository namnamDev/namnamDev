def my_func(T):
    for i in range(T):
        N = int(input())
        printN = N
        cnt = 1
        plus = 1
        i = 0
        j = -1
        my_list = [[0 for i in range(N)] for j in range(N)]
        while N > 0:
            for a in range(N):
                j += plus
                my_list[i][j] = cnt
                cnt += 1
            N -= 1
            for b in range(N):
                i += plus
                my_list[i][j] = cnt
                cnt += 1
            plus *= -1
        for i in range(printN):
            for j in range(printN):
                print('{:02}'.format(my_list[i][j]),end=' ')
            print()
        print()