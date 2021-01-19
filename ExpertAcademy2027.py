# print('#++++')
# print('+#+++')
# print('++#++')
# print('+++#+')
# print('++++#')
for i in range(5) :
    a = ''
    for g in range(5): 
        if i==g :
            a +='#'
        else :
            a+='+'
        print(f'{a}')