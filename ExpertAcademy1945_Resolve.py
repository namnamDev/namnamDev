import sys
sys.stdin =open("ExpertAcademy1945_Resolve.txt")
def counting(N, nums) :
    cnt = 0
    t = N
    while not t % nums:
        t = t//nums
        cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    an = ""
    li = [2, 3, 5, 7, 11]
    for i in li:
        an += str(counting(N, i)) + " "
    print("#{} {}".format(tc, an))
