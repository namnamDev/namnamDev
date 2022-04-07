def top():
    for i in range(1, ga - 1):
        one_block[0][i] = "-"


def mid():
    for i in range(1, ga - 1):
        one_block[(s * 2 + 3) // 2][i] = "-"


def bot():
    for i in range(1, ga - 1):
        one_block[-1][i] = "-"


def r_t():
    for i in range(1, se_one):
        one_block[i][-1] = "|"


def r_b():
    for i in range(se_one + 1, s * 2 + 2):
        one_block[i][-1] = "|"


def l_t():
    for i in range(1, se_one):
        one_block[i][0] = "|"


def l_b():
    for i in range(se_one + 1, s * 2 + 2):
        one_block[i][0] = "|"


a, b = input().split()
s = int(a)
se_one = (2 * s + 3) // 2
ga = s + 2
an_list = [[] for _ in range(2 * s + 3)]
for al in b:
    one_block = [[" "] * ga for _ in range(2 * s + 3)]
    if al == "1":
        r_t()
        r_b()
    elif al == "2":
        top()
        mid()
        bot()
        r_t()
        l_b()
    elif al == "3":
        top()
        mid()
        bot()
        r_b()
        r_t()
    elif al == "4":
        mid()
        r_t()
        l_t()
        r_b()
    elif al == "5":
        top()
        mid()
        bot()
        l_t()
        r_b()
    elif al == "6":
        top()
        mid()
        bot()
        l_b()
        r_b()
        l_t()
    elif al == "7":
        top()
        r_t()
        r_b()
    elif al == "8":
        top()
        mid()
        bot()
        l_t()
        l_b()
        r_t()
        r_b()
    elif al == "9":
        top()
        mid()
        bot()
        l_t()
        r_t()
        r_b()
    elif al == "0":
        top()
        bot()
        l_t()
        l_b()
        r_t()
        r_b()
    for ff in range(2 * s + 3):
        an_list[ff] += ["".join(one_block[ff])]

for an in an_list:
    print(*an)
