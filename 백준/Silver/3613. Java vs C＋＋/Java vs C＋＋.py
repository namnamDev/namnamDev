def c_to_java(p_word):
    for w in p_word:
        if 65 <= ord(w) <= 90:
            return "Error!"
    arr = p_word.split("_")
    temp_answer = ""
    for w in arr:
        if not len(w):
            return "Error!"
        t = list(w)
        t[0] = t[0].upper()
        temp_answer += "".join(t)
    aa = list(temp_answer)
    aa[0] = aa[0].lower()
    return "".join(aa)


def java_to_c(p_word):
    arr = []
    if 65 <= ord(p_word[0]) <= 90:
        return "Error!"
    temp_word = ""
    for w in p_word:
        if 65 <= ord(w) <= 90:
            arr.append(temp_word)
            temp_word = w.lower()
        else:
            temp_word += w
    arr.append(temp_word)
    return "_".join(arr)


word = input()
answer = ""
if word.find("_") >= 0:
    answer = c_to_java(word)
else:
    answer = java_to_c(word)
print(answer)