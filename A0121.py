def my_abs(a):
    if a<0 :
        print(-a)
        return -a
    # elif a = 0

# num = int(input())
# my_abs(num)
# print(type(4j/1j))

def my_all(a):
    result = True
    temp = True
    temp2 = True
    for i in a :
        if type(i) == (list or tuple or dict):
            print(i)
            temp = my_all(i)
        else:
            if bool(i) :
                temp2 =  True
            else :
                temp2 = False
        if temp != temp2:
            result = False
            break
    return result
a = [[],[],[],[]]
b = []
# print(f'sample {bool(b==None)}')
print(my_all([])) #=> True
print(my_all([1, 2, 5, '6'])) #=> True
print(my_all([[[],[]], 2, 5, '6'])) #=> False
# print(*[[], 2, 5, '6'])
# print([[], 2, 5, '6'])