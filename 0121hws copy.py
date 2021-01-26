#List Comprehension
# lists = [ i**3 for i in range(1,10)]
# print(lists)
# listss = [if i%2==0 for i in range(1,10)]
# print(listss)
# listsss = [ for i in range(1,10) if i%2 == 0]
# print(listsss)

# lists_1 = [1,2,3,4,5,9,9,9]
# lists_2 = [6,7,8,9,0]
# def addList(*args) : 
#     return args[0] + args[1]

# result = list(map(addList , lists_1,lists_2))
# print(result)
# set_a = {1,2,3,4,5,6}
# set_b = set_a.pop()
# print(set_a)

vowels = ['a','e','i','o','u']
def count_vowels(strings) :
    cnt = 0
    for i in vowels :
        cnt += strings.count(i) 
    print(cnt)
    return cnt
    
    

count_vowels('apple') #=>2
count_vowels('banana') #=>3

dir('string')
