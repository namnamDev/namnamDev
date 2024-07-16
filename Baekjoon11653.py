import sys
from pathlib import Path

sys.stdin = open(Path(__file__).stem + ".txt")
N = int(input())
i = 2
while N != 1:
    if N % i:
        i += 1
    else:
        N //= i
        print(i)