from collections import deque

start = input()
end = input()
end_size = len(end)
start_size = len(start)
Q = deque([end])
an = 0
used = {}
while Q:
    now = Q.popleft()
    if now == start:
        an = 1
        break
    if len(now) > start_size:
        if now[0] == "B":
            b_now = now[:0:-1]
            Q.append(b_now)

        if now[-1] == "A":
            a_now = now[:-1]
            Q.append(a_now)
print(an)