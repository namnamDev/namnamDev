import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy1216.txt")
def palindrom(i):
    for f in range(i):
        for g in range(i):
            li[f][g] == li[f][g+N+1-i]




for tc in range(1,11):
    N = 100
    li = [0]*N
    tcc = int(input())
    for g in range(100):
        li[g] = input()
    pprint(li)
    for i in range(N,0,-1):
        an = palindrom(i)
