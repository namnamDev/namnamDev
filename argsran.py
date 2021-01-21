def my_max(*args) :
    max = 0
    for i in args:
        if max < i:
            max = i
    return max

print(my_max(10, 20, 30, 50))
