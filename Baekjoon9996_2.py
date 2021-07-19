import sys

sys.stdin = open('Baekjoon9996.txt')
N = int(input())
sample = list(input().split('*'))  # 입력된 단어를 *로 나누어 앞단어 뒷단어로 저장
arr = [input() for _ in range(N)]  # 입력된 문장들 입력예정
answer = ['0'] * N  # 정답리스트 저장할것들
# print(sample)
fir = sample[0]
sec = sample[1]
print(len(fir), len(sec))
for i in range(N):
    firstIdx = -3
    secIdx = -3  # 초기값을 불가능한 값으로 설정
    line = arr[i]
    print(len(line), len(line) - len(fir) + 1)
    for f in range(len(line) - len(fir) + 1):
        print(line[f:f + len(fir)], fir)
        if line[f:f + len(fir)] == fir:  # 문자열 자르기로 비교
            # print(line[f:f + len(fir)] == fir)
            firstIdx = f  # 만약 문자열 잘랐을때 같다면 firstIdx를 현재 인덱스로 저장함
            break

    print(firstIdx + len(fir), len(line) - len(sec) + 1)
    if firstIdx == -3:  # 만약 첫번째 인덱스가 변하지 않았다면
        answer[i] = "NE"  # 불가능하다

    else:  # 첫번째 인덱스가 변했다 = 첫번째 단계를 통과했다
        for g in range(firstIdx + len(fir), len(line) - len(sec) + 1):
            print(line[g:g + len(sec)], sec)
            if line[g:g + len(sec)] == sec:
                # print(line[g:g + len(sec)] == sec)
                secIdx = g
                answer[i] = "DA"
                break
    if secIdx == -3:
        answer[i] = "NE"
for ii in answer:
    print(ii)
