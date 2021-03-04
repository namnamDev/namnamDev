import sys

sys.stdin = open("Baekjoon14888.txt")


def oper(N):
    global ansli
    if used == operator or 0 not in position:
        ans = arr[0]

        # print(position)
        for i in range(len(position)):
            aa = position[i]
            nums = arr[i + 1]
            # print(arr[i])
            if aa == 1:
                ans += nums
            elif aa == 2:
                ans -= nums
            elif aa == 3:
                # print(ans, nums)
                ans *= nums
            else:
                if ans < 0:
                    ans *= -1
                    ans //= nums
                    ans *= -1
                else:
                    ans //= nums
        # print(ans)
        ansli += [ans]
        return
    else:
        for i in range(1, 5):
            if used[i] != operator[i] and position[N] == 0:
                used[i] += 1
                position[N] = i
                oper(N + 1)
                used[i] -= 1
                position[N] = 0


N = int(input())
arr = list(map(int, input().split()))
operator = [0] + list(map(int, input().split()))
position = [0] * (N - 1)
used = [0] * 5
ansli = []
oper(0)
print(max(ansli))
print(min(ansli))
