import sys
N = sys.stdin.readline().split()
def myRev(a):
    max =0
    result = a[::-1] # 알아서 str형태로 들어온다
    return result

samples = []
for i in N:
    samples += [int(myRev(i))]
if samples[0] < samples[1] :
    print(samples[1])
else :
    print(samples[0])
