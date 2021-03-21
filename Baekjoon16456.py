def powserset(num, arr):
    if 0 not in visited:
        global cnt
        cnt += 1
        return
    else:
        for i in range(3):
            wn = num + dirs[i]
            if 0 <= wn < T:
                if visited[wn] == 0:
                    visited[wn] = 1
                    powserset(wn, arr + [dirs[i]])
                    visited[wn] = 0


dirs = [-1, 1, 2]
T = int(input())
visited = [0] * T
visited[0] = 1
cnt = 0
Q = [0]
arr = []
# powserset(0, [])
while len(Q):
    print(Q)
    now = Q.pop()
    for i in range(3):
        wn = now + dirs[i]
        if 0 <= wn < T:
            if visited[wn] == 0:
                Q.append(wn)
                arr += [dirs[i]]
                visited[wn] = 1

# print(cnt % 1000000009)
