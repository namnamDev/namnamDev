T = int(input())
lists = []
for i in range(T):
    lists.append(input())
lists = list(set(lists))
lens = len(lists)
print(lists)
for i in range(lens) :
    for g in range(lens):
        if len(lists[g]) >len(lists[i]):
            print(lists[g],lists[i])
            lists[i] , lists[g]= lists[g] , lists[i]
            print(lists[g],lists[i])
            print(lists)

        if len(lists[g]) == len(lists[i]):
            print('----')
            for numnum in len(lists[g]):
                if ord(lists[g]) > ord(lists[i]) :
                    lists[i] , lists[g]= lists[g] , lists[i]
                    break
            print('----')
            print(lists)