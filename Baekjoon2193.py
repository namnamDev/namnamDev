import sys

sys.stdin = open('Baekjoon2193.txt')


# def leechinSoo(arr):
#     if len(arr) == :
#         return 1
#     else:
#         if arr[-1] == 1:
#             vi[len(arr)] += leechinSoo(arr[:len(arr)])
#         else:
#             vi[len(arr)] += leechinSoo(arr[:len(arr)])
#             vi[len(arr)] += leechinSoo(arr[:len(arr)])


def lee(a):
    if a <= 3:
        return vi[a]
    else:
        vi[a] = vi[a - 1]


N = int(input())
vi = [0] * (N + 1)
vi[1] = 1
vi[2] = 1
vi[3] = 2
leechinSoo([1])
print(vi)
