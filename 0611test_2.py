import sys

sys.stdin = open('0611test_2.txt')


def aa(depth, idx, left, right):
    # print(depth, idx, left, right)
    if idx == N - 1:
        # print(left, right, abs(sum(left) - sum(right)))
        answer.append(abs(sum(left) - sum(right)))
        return
    else:
        for i in range(idx + 1, N):
            if not vi[i]:
                vi[i] = 1
                aa(depth + 1, i, left + [arr[i]], right)
                aa(depth + 1, i, left, right + [arr[i]])
                vi[i] = 0
                aa(depth + 1, i, left, right)


N = int(input())
arr = list(map(int, input().split()))
vi = [0] * (N)
print(N)
print(arr)
answer = []
aa(0, -1, [], [])
print(set(answer), len(set(answer)))
