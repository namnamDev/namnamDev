def is_pal_while(word):
    result = True
    cnt = 0
    for i in word: ## 크기
        cnt += 1
    cnt2 = 0
    div = cnt//2 
    while cnt2 < div :
        if word[cnt2] != word[cnt-1-cnt2]:
            result = False
            break
        else :
            cnt2+=1
    return result

def is_pal_recursive(word):
    cnt =0
    answer = True
    for i in word:
        cnt+=1
    if cnt != 0:
        if word[0] == word[cnt-1]:
            word = word[1:cnt-1]
            is_pal_recursive(word)
        else :
            answer = False
    return answer

# 해당 코드를 통해 올바른 결과가 나오는지 확인하시오.
print(is_pal_while('tomato'))
print(is_pal_while('racecar'))
print(is_pal_while('azza'))
print('-------------')
print(is_pal_recursive('tomato'))
print(is_pal_recursive('racecar'))
print(is_pal_recursive('azza'))