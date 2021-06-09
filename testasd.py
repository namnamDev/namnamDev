# aa = input()
# #ASADADAS
# bb = [0]*120
# for i in aa:
#     bb[ord(i)]+=1
# answer = bb.index(max(bb))
# print(chr(answer),max(bb))
temp = input() #SSADADAAASADAAAS
N = 5
answers = [0]*100
for i in range(len(temp)-N):
    cnt = [0]*100
    templist = temp[i:i+N]
    for i in templist:
        # print(i)
        cnt[ord(i)]+=1
    answers[cnt.index(max(cnt))]+=1
    # print(templist)
# print(answers)
print(chr(answers.index(max(answers))))
