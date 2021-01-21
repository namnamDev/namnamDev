dics = { '123' : 232, 123:'ss332',1:23}

def lendic(a) :
    cnt = 0
    for i in a:
        print(f'key : {i} value :{dics[i]} keytype : {type(i)} valuetype : {type(dics[i])}')
        cnt+=1
    return cnt

def stu(*args , prof):
    for num in args:
        print(num)
    print('+++'+prof+'+++')

stu( '1','2','3', prof = '2')
print(lendic(dics))

def makeURL(**kwlist):
    myUrl = "http://192.168.1.120/index.php?"
    print(kwlist.items())
    for k, v in kwlist.items():
        myUrl += k + '=' + v + '&'

    myUrl = myUrl.rstrip('&')
    print(myUrl)

makeURL(user = 'psychoria', index = '5', page = '10')