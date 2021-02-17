import sys
sys.stdin = open("ExpertAcademy1221.txt")
nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for tc in range(1, T+1):
    tcc, N = input().split()
    li = input().split()
    countli = [0]*10
    intN = int(N)
    for i in range(intN) :
        for g in range(10):
            if nums[g] == li[i]:
                li[i] = g
                countli[g] += 1
    ans = []
    for ff in range(10):
        for gg in range(countli[ff]):
            ans += [nums[ff]]
    # for f in range(1, 10):
    #     countli[f] += countli[f-1]
    ans = " ".join(ans)
    print(tcc)
    print(ans)