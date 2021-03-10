import sys

sys.stdin = open("Baekjoon16457.txt")

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
visited = [0] * (2 * n + 1)
an = 0
st = list(range(1, n + 1))

while len(st) != 0:
    print(st, an)
    te2 = 0
    if len(st) == n:
        for i in range(m):
            te = 0
            for g in range(k):
                if arr[i][g] in st:
                    te += 1
            if te == k:
                te2 += 1
        if an < te2:
            an = te2
    temp = st.pop()
    wt = temp
    while len(st) < n:
        wt += 1
        if wt <= 2 * n:
            st.append(wt)
        else:
            break
print(an)
