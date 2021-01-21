def get_secret_word(lists) :
    answer = ''
    for i in lists :
        answer += chr(i)
    return answer

def get_secret_number(name) :
    answer = 0
    for i in name :
        answer += ord(i)
    return answer

def get_strong_word(name1, name2) :
    answer1 = 0
    answer2 = 0
    answer = ''
    for i in name1 :
        answer1 += ord(i)
    for i in name2 :
        answer2 += ord(i)
    if answer1>answer2 :
        answer = name1
    else :
        answer = name2
    return answer

print(get_secret_word([83, 115, 65, 102, 89])) #=>SsAfY
print(get_secret_number('tom'))
print(get_strong_word('z', 'a'))
print(get_strong_word('tom', 'john'))
