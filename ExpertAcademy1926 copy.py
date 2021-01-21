def func(x):
    A = []
    for i in range(1, x+1):
        si = str(i)
        cnt = 0
        for j in si:
            if j in ['3', '6', '9']:
                cnt += 1
        if cnt == 0:
            A.append(i)
        else:
            A.append('-' * cnt)

    return *A

result = func(num)
print(result)