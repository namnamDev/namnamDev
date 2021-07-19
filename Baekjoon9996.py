import sys

sys.stdin = open('Baekjoon9996.txt')
N = int(input())
sample = list(input().split('*'))  # *으로 앞 뒤 구분함
arr = [input() for _ in range(N)]  # 입력되는 문구를 배열로 저장
answer = [''] * N
for i in range(N):
    firstIdx = -1
    secIdx = 0
    line = arr[i]
    fir = sample[0]  # 앞단어
    sec = sample[1]  # 뒷단어
    for g in range(len(line) - len(fir)):  # 첫번째 단어의 길이 한자한자 비교
        # for f in range(len(fir)):  # 앞단
        print(line[g:g + len(fir) + 1])
        if line[g:g + len(fir) + 1] == fir:
            firstIdx = g
            break
        # if line[g:g + f + 1] == fir:
        #     firstIdx = g
        #     break

    if firstIdx == -1:
        answer[i] = "NE"
    else:
        for f in range(firstIdx - 1 + len(fir), len(line)):
            if line[f:f + len(sec) + 1] == sec:
                firstIdx = g
                break
            # if line[f] == sample[1]:
            #     secIdx = f
            #     answer[i] = "DA"
            #     break
    if not secIdx:
        answer[i] = "NE"
for ii in answer:
    print(ii)
