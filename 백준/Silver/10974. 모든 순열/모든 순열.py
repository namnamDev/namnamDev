def my_lec(arr):
    if len(arr) == a:
        print(*arr)
        return
    for i in range(a):
        if not vi[i]:
            vi[i] = 1
            my_lec(arr + [i + 1])
            vi[i] = 0


a = int(input())
vi = [0] * a
my_lec([])
