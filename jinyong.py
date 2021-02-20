# print('hello world')

# a = 110
# hello = "hello"
# print(type(a))
# print(type(hello))
#
# n1 = 5
# n2 = 3
# an = n1 + n2
# an = 5/3
# an = 5//3
# an = 5 % 3
# liRange = list(range(5))
# print(liRange)
mutables = [1, 2, 3, 4] #값변경 가능하다! mutable
a = mutables
print(a)
mutables += [5]
b = mutables
print(b)
mutables = {1, 2, 3, 4} #값변경 가능하다! mutable
a = mutables
print(id(mutables))
mutables = {1, 2, 3, 4, 5}
b = mutables
print(id(mutables))
print(a)
print(b)
# print(type(lists))
# print(type(sets))
# print(type(tuples))
# print(type(dicts))
# tuple set dict
