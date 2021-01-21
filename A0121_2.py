def snail(a,b,c) :
    answer = (a-b)/(b-c)+1
    temp = (a-b)//(b-c)+1
    yingyou  = answer - temp 
    if yingyou != 0 :
        answer = answer + 1 -yingyou #하루 더 올리고 정수뺴기
    answer = int(answer)
    return answer

# print(snail(100 , 5, 2))
# print(snail(6 , 5, 1))
# print(snail(1000000000 , 100 , 99))

print(int(1.5))
# N-1일간 총 거리 = (b-c)*(N-1)
# N일 낮 거리 = (b-c)*(N-1)+b > a
# 32일 낮 거리 = 31*3+5 = 93+5 98
# 32일간 간 거리  = 32*3 = 96
# 33일 낮 거리 = 32*3 + 5 
# 
# N = (a-b)/(b-c) + 1

def sum_of_digit(intNum):
    temp = str(intNum)
    sum = 0
    for i in temp :
        sum += int(i)
    return sum


print(sum_of_digit(1234))
print(sum_of_digit(4321))
print(sum_of_digit(432111111))