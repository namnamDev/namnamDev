def fib_loop(n):
    # a, b = 0 , 1
    a = 0
    b = 1
    cnt = 1
    while cnt < n:
        cnt +=1
        a,b = b, a+b
    return b

print(fib_loop(11))