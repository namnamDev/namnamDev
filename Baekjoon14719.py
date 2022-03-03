import sys
from pathlib import Path

sys.stdin = open(Path(__file__).stem + ".txt")

# def aa(dept,fir,sec):
#     if not dept:
#         return
#     else:


H, W = map(int, input().split())
arr = list(map(int, input().split()))
vi = [0] * W
for e in range(H, -1, -1):
    tarr = []
    for i in range(W):
        if arr[i] <= e:
            tarr.append(i)
    # if len(tarr)>=2:

# while fir < W:
#     if arr[fir]:
#         for tsec in range(fir + 1, W):
#             if arr[fir] <= arr[tsec]:
#                 sec = tsec
#                 break
#     fir += 1
#
# for fir in range(W):
#     if arr[fir]:
#         for sec in range(fir + 1, W):
#             if arr[fir] < arr[sec]:
#                 break
