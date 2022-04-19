N = int(input())
arr = [input()[::-1] for _ in range(N)]
an = len(arr[0])
for i in range(1, an + 1):
    dict = {}
    cnt = 0
    for t in arr:
        if dict.get(t[:i]):
            break
        else:
            dict[t[:i]] = 1
            cnt += 1
    if N == cnt:
        an = i
        break
print(an)