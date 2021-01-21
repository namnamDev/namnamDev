def self_num(a):
    # print(a)
    sums = 0
    if a<10000:
        strA = str(a)
        sums = a
        for i in strA:
            sums += int(i)
        print(sums)
        lists[sums] =0
        self_num(sums)
    # return num
        

lists = list(range(10001))
# print(lists)
self_num(1)
lists = set(lists)
for i in lists:
    print(i)