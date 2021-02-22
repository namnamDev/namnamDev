answer = {}
T = int(input())
for i in range(T):
    case_result = [[1], [1, 1]]
    N = int(input())
    temp = ''
    if (N == 1):
        case_result = [[1]]
    else:
        for g in range(2, N):
            temp_1 = []
            for line in range(g + 1):
                ones = 0
                if line == 0 or line == g:
                    ones = 1
                else:
                    sik = case_result[g - 1][line - 1] + case_result[g - 1][line]
                    ones = sik
                temp_1.append(ones)
            case_result.append(temp_1)
    answer[i] = case_result

for i in range(T):
    print('#{}'.format(i + 1))
    for g in answer.get(i):
        print(*g)
