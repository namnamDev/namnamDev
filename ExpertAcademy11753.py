import sys

sys.stdin = open('ExpertAcademy11753.txt')
for tc in range(1, int(input()) + 1):
    val = float(input())
    ret = []
    S = ['9', '9']

    while (S[1] != '0' and len(ret) <= 12):
        val *= 2
        S = str(val).split('.')
        ret.append(S[0])
        val = float('0.' + S[1])
    if len(ret) >= 13:
        print('#{} overflow'.format(tc))
    else:
        print("#{}".format(tc), ''.join(ret))
