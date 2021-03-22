def solution(s):
    answer = len(s)
    for y in range(1, len(s) // 2 + 1):
        idx = y
        temp = s[:y]
        an = ''
        tempcnt = 1
        while idx < len(s):
            # print(temp,s[idx:idx+y],tempcnt)
            if temp == s[idx:idx + y]:
                tempcnt += 1
            else:
                if tempcnt <= 1:
                    an += temp
                else:
                    an += str(tempcnt) + temp
                    # print(an)
                temp = s[idx:idx + y]
                tempcnt = 1
            idx += y
        if tempcnt <= 1:
            an += temp
        else:
            an += str(tempcnt) + temp
        # print(y,an)
        # print(an,answer)

        if len(an) < answer:
            answer = len(an)
    return answer
