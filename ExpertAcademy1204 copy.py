T = int(input())

for tc in range(1,T+1):
    test_num = int(input())
    case = [*map(int,input().split())]

    dic = {}
    for i in case:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    print(dic)
    max_dic = {}
    for j in case:
        if dic[j] == max(dic.values()):
            max_dic[j] = dic[j]

    print(f'#{test_num} {max(max_dic.keys())}') 