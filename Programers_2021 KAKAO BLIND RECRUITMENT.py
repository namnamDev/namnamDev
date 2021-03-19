maxCnt = 2
maxArr = []
res = []


def solution(orders, course):
    answer = []
    temp = []
    board = []
    for i in orders:
        for g in i:
            if g not in temp:
                temp.append(g)

    temp.sort()

    def powerset(nums, arr):
        global maxCnt
        global maxArr
        global res
        if len(arr) == i:
            cnt = 0
            for one in orders:
                tempcnt = 0
                for g in arr:
                    if g in one:
                        tempcnt += 1
                if tempcnt == i:
                    cnt += 1
            if maxCnt <= cnt:
                maxCnt = cnt
                maxArr = arr
                res[maxCnt].append(maxArr)
            return
        if nums == len(temp):
            return
        else:
            powerset(nums + 1, arr + [temp[nums]])
            powerset(nums + 1, arr)

    answer = []
    for i in course:
        global res
        global maxCnt
        global maxArr
        res = [[] for _ in range(len(orders))]
        powerset(0, [])
        if res[maxCnt]:
            for i in res[maxCnt]:
                ans = ""
                for g in i:
                    ans += g
                answer.append(ans)
        maxCnt = 2
        maxArr = []
    answer.sort()
    return answer
