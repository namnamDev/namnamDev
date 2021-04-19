import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy1256.txt")

for tc in range(int(input())):
    N = int(input())
    word = input()
    len_word = len(word)
    words = []
    for i in range(len_word):
        words.append(word[i:len_word])
    words.sort()
    print("#{} {}".format(tc + 1, words[N - 1]))
