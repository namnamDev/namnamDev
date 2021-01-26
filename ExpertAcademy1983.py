T = int(input())
for start in range(1,T+1):
    TC = list(map(int,input().split()))
    N,K = TC[0],TC[1]
    arr = {}
    for num in range(1,N+1) :
        scrs = list(map(int,input().split()))
        scr = (scrs[0]*35) + (scrs[1]*45) + (scrs[2]*2)
        arr[num] = scr
    # print(arr)
    arr = sorted(arr, key= lambda x : arr[x] ,reverse=True)
    grade_list = ['A+' , 'A0', 'A-','B+','B0','B-','C+','C0','C-','D0']
    rank = N//10
    grade_list = grade_list*rank
    answer = grade_list[K]
    print(f'#{start} {answer}')
    # print(arr)
    # print(len(arr))



