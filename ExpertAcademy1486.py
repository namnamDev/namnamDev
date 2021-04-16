import sys

sys.stdin = open("ExpertAcademy1486.txt")


def powerset(num, idx):
    if num >= M:
        global an
        an = min(an, num - M)
        return
    else:
        for g in range(idx + 1, N):
            if not visited[g]:
                visited[g] = 1
                powerset(num + arr[g], g)
                visited[g] = 0


for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    an = M
    for i in range(N):
        visited = [0] * N
        visited[i] = 1
        powerset(arr[i], i)
    print("#{} {}".format(tc + 1, an))
