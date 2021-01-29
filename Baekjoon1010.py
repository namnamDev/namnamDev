NM = list(map(int,input().split()))
N = NM[0]
M = NM[1]
max_down = M-N+1
#4 7
#1[1] 2[2] 3[3] 4[4~7] 4
#1[1] 2[2] 3[4] 4[5~7] 3
#1[1] 2[2] 3[5] 4[6~7] 2
#1[1] 2[2] 3[6] 4[7]   1 10

#1[2] 2[3] 3[4] 4[5~7] 3
#1[2] 2[3] 3[5] 5[6~7] 2
#1[2] 2[3] 3[6] 5[7]   1 6

#1[3] 2[4] 3[5] 4[6~7] 2
#1[3] 2[4] 3[6] 4[7]   1 3

#1[4] 2[5] 3[6] 4[7]   1 1

#1[1] + 1[2] + 1[3] + 1[4] +1[5]
#1*4 +2*3 + 3*2+4*1 = 4+4+6+6 = 20
sums = 0
temp = 1
cnt = M-N+2 # 7-4 +1 = 4
for i in range(1,cnt) : 
    sums += i*(cnt-i)
    print(f'{i}*{cnt-i}')
print(sums)
# for left in range(N):
#     print(left)
#     while cnt != 0 :
#         for i in range(1,cnt+1) :
#             temp = temp*i
#             print(f'temp는 {temp}')
#             cnt -= 1
#             print(temp)
#     sums += temp
#     temp = 1
#     cnt = M-left+1
# print('----')
# print(sums)
# print('----')