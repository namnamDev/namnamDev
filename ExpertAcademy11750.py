import sys

sys.stdin = open('ExpertAcademy11750.txt')
for tc in range(int(input())):
    N, N16 = input().split()
    N = int(N)
    an = ''
    for i in range(N):
        temp = 0
        temp_N16 = N16[i]
        if temp_N16.isdigit():
            temp = int(temp_N16)
        else:
            temp = ord(temp_N16) - 55
        bins = ''
        while temp:
            bins = str(temp % 2) + bins
            temp //= 2
        while len(bins) < 4:
            bins = '0' + bins

        an += bins
    print("#{} {}".format(tc + 1, an))
# 1 0100011111111110
# 1 0100011111111110
# 2 01111001111000010010
# 2 01111001111000010010
# 3 01000001110110100001011011001101
