N = int(input())
visit = [0] * 10
answer_list = []

for i in range(1, 10):
    if not visit[i]:
        visit[i] = 1
        for j in range(1, 10):
            if not visit[j]:
                visit[j] = 1
                for f in range(1, 10):
                    if not visit[f]:
                        visit[f] = 1
                        answer_list.append(str(i) + str(j) + str(f))
                        visit[f] = 0
                visit[j] = 0
        visit[i] = 0

answer_yn = [1] * len(answer_list)

arr = [list(map(int, input().split())) for _ in range(N)]

for num, strike, ball in arr:
    for target_num_idx in range(len(answer_list)):
        if answer_yn[target_num_idx]:
            str_num = str(num)
            num_v = [0] * 3
            for idx in range(3):
                if (not num_v[idx]) and answer_list[target_num_idx][idx] == str_num[idx]:
                    num_v[idx] = 2
                if (not num_v[idx]) and answer_list[target_num_idx].find(str_num[idx]) != -1:
                    num_v[idx] = 1
            if (num_v.count(2) == strike) and (num_v.count(1) == ball):
                pass
            else:
                answer_yn[target_num_idx] = 0
print(answer_yn.count(1))
