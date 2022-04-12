def lec(idx, p_opers, p_sum, last_num):
    if idx == a:
        if p_sum + last_num == 0:
            an_list.append(p_opers)
        return
    t_idx = idx + 1

    lec(t_idx, p_opers + "+" + str(t_idx), p_sum + last_num, t_idx)
    lec(t_idx, p_opers + "-" + str(t_idx), p_sum + last_num, -t_idx)
    lec(t_idx, p_opers + " " + str(t_idx), p_sum, int(str(last_num) + str(t_idx)))


T = int(input())
arr = []
for tc in range(T):
    arr.append(int(input()))
operations = ["+", "-", " "]
for a in arr:
    an_list = []
    lec(1, "1", 0, 1)
    an_list.sort()
    for i in an_list:
        print(i)
    print()