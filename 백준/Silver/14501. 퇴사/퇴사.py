def my_back(day, res):
    if day >= N:
        return
    for start_date in range(day, N):
        if not work[start_date]:
            end_work_date = start_date + arr[start_date][0]
            if end_work_date <= N:
                for idx in range(start_date, end_work_date):
                    work[idx] = 1
                valueList.append(res + arr[start_date][1])

                my_back(start_date + 1, res + arr[start_date][1])

                for reversIdx in range(end_work_date - 1, start_date - 1, -1):
                    work[reversIdx] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
work = [0] * N
valueList = [0]
my_back(0, 0)
print(max(valueList))