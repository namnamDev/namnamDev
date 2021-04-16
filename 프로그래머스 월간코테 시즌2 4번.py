res = 0


def solution(n, z, roads, queries):
    answer = []
    point = []
    for i in roads:
        point.append(i[1])

    def dfs(nums, cnt, idx):
        global res
        if res < cnt:
            return
        if nums > queries[ff]:
            return
        if nums == queries[ff]:
            res = min(res, cnt)
            return
        # 안움직이기
        dfs(nums + z, cnt + 1, idx)
        # 그냥 가기
        for i in range(len(roads)):
            if roads[i][0] == idx:
                dfs(nums + roads[i][2], cnt + 1, roads[i][1])
            else:
                dfs(nums, cnt + 1, roads[i][0])
        # 순간이동하기
        # if not teleport:
        #     for g in roads:
        #         if idx != g[1]:
        #             dfs(nums,cnt+1,g,1)

    for ff in range(len(queries)):
        global res
        res = n * n
        dfs(0, 0, 0)
        if res == n * n:
            answer.append(-1)
        else:
            answer.append(res)

    return answer
