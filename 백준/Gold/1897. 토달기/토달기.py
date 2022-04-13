def lec(p_word):
    if used_word[p_word]:
        return
    used_word[p_word] = 1
    global long_word
    p_size = len(p_word)
    if len(long_word) < p_size:
        long_word = p_word
    t_tree = word_dic.get(len(p_word) + 1)
    if not t_tree:
        return
    else:
        for t_one in t_tree:
            cnt = 0
            f_idx = 0
            t_idx = 0
            while f_idx < p_size and t_idx < len(t_one):
                if p_word[f_idx] == t_one[t_idx]:
                    f_idx += 1
                else:
                    cnt += 1
                t_idx += 1
            if cnt <= 1:
                lec(t_one)


N, start = input().split()
N = int(N)
i = 0
tree = [0] * N
word_dic = {}
word_dic2 = {}
used_word = {}
for n in range(N):
    a = input()
    a_size = len(a)
    used_word[a] = 0
    if not word_dic.get(a_size):
        word_dic[a_size] = [a]
    else:
        word_dic[a_size].append(a)
long_word = ""
lec(start)
print(long_word)