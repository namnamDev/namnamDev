def check_p(num):
    temp_str = str(num)
    revers_str = temp_str[::-1]
    if temp_str != revers_str:
        return False
    return True


N = int(input())
max_size = 1003002
arr = [0] * max_size
arr[0] = arr[1] = 1
for i in range(2, max_size):
    num = i * 2
    while num < max_size:
        if not arr[num]:
            arr[num] = 1
        num += i
    if not check_p(i):
        arr[i] = 1

    if N <= i and not arr[i]:
        print(i)
        break
