arr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
target = list(input())
visited = [0] * len(target)
cnt = 1
for i in range(len(target)):
    if not visited[i]:
        for compare in arr:
            if "".join(target[i:i + len(compare)]) == compare:
                for ti in range(i, i + len(compare)):
                    visited[ti] = cnt
                cnt += 1

answer = visited.count(0) + len(set(visited))
if visited.count(0):
    answer -= 1
print(answer)