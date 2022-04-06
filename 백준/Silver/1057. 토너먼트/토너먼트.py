N, a, b = map(int, input().split())
a -= 1
b -= 1
arr = list(range(N))
cnt = 0
answer = 0
while not answer:
    t = []
    cnt += 1
    for i in range((len(arr)) // 2):
        left = arr[2 * i]
        right = arr[2 * i + 1]
        if (left == a and right == b) or (left == b and right == a):
            answer = cnt
            break
        else:
            if left == a or left == b:
                t.append(left)
                continue
            if right == a or right == b:
                t.append(right)
                continue
            t.append(left)
    if len(arr) % 2:
        t.append(arr[-1])

    if not t and not answer:
        answer = -1
    arr = t

print(answer)
