X, Y = map(int, input().split())
cnt = (-X / 100) / (Y / X - 0.99)
if int(cnt * 10) % 10:
    cnt += 1
if Y / X >= 0.99:
    cnt = -1
print(int(cnt))
# 48
# 470000000+cnt /1000000000+cnt = 48
# 470000000/1000000000 = 47
# 470000000 + 1000000000 / 1000000000 = 470000000+cnt /1000000000+cnt
# 1000000000+cnt(470000000 + 1000000000) = (470000000+cnt) 1000000000
# X + cnt (X+Y) = (Y+cnt)X
# X+ cntX +cntY = YX +cntX
# -X+YX = cntY
# cnt =(YX-X)/Y
# cnt = X(Y-1)/Y
# (Y+cnt)/(X+cnt)- Y/X = 1
# (Y+cnt)/(X+cnt)= 1 + Y/X
# Y+cnt = ((1+Y)/X)(X+cnt)
# XY + cntX = X+cnt+XY +cntY
# cntX-cntY -cnt= X
# cnt(X-Y-1) = X
# cnt = X/(X-Y-1)
# Y/X+1/100  = (Y+cnt)/(X+cnt)
# (X+cnt)*Y/X + (X+cnt)/100 = Y+cnt
# (XY+cntY)/X + X/100+cnt/100 = Y+cnt
# Y + cntY/X +X/100 +cnt/100 = Y+cnt
# cnt*Y/X +cnt/100 - cnt = -X/100
# cnt(Y/X-99/100) = -X/100
# cnt = (-X/100)/(Y/X-0.99)

# (100*Y)(X+cnt)/X = Y+cnt
# 100XY+100cntY = XY + cntX
# cnt(100Y-X) = XY-100XY
# cnt = (X*Y-100*X*Y) / (100*Y-X)
