def my_dict(**kwargs):
    print(type(kwargs))
    return kwargs

print(my_dict(한국어='안녕', 영어='hi', 독일어='Guten Tag'))
