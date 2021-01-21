def f1(x):
    return cnt[x]

case = int(input())
for i in range(case):
    casenum = int(input())
    grades = list(input().split())
    cnt = {}
    for j in grades:
        cnt[j] = grades.count(j)

    cnt_max = max(cnt.keys(), key=f1)
    print('#{} {}'.format(i+1, cnt_max))
    
my_dict {
    'a' : 1,
    'b' : 2,
    'c' : 5,
    'd' : 4
}