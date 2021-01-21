# def get_middle_char(a):
#     cnt = 0
#     answer = ''
#     for i in a:
#         cnt+=1
    
#     if cnt%2 :
#         temp = cnt//2
#         answer = f'{a[temp-1]}{a[temp]}'
#     else:
#         temp = cnt//2
#         answer = f'{a[temp]}'
#     return answer

# get_middle_char('ssafy')
# get_middle_char('coding')

def list_sum(args):
    sums = 0
    for i in args:
        sums+=i
    print (sums)
list_sum([1,2,3,4,5])
