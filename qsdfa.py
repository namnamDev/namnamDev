def get_middle_char(x):

    i = len(x)//2

    if i & 1 :
        a = x[i]
    else:
        a = x[i-1],x[i]
    return a

