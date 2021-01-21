T = int(input())

def my_func(T):
    # word = [ ['A','3'] , ['B','2'] , ['C','5'] ]
    for i in range(T):
        print('#'+str(i+1),end='')

        N = int(input())

        word = []
        for i in range(N):
            word.append(input().split())    

        new_word = []
        for i in word:
            for j in range(int(i[1])):
                new_word.append(i[0])

        cnt = 0
        for i in new_word:
            if cnt % 10 != 0:
                print(i,end='')
            else:
                print('\n',i,end='')
            cnt += 1
        
        print()

my_func(T)