xs, ys = map(int, input().split())
xe, ye, dx, dy = map(int, input().split())
t = 0
mins = (xs - xe) ** 2 + (ys - ye) ** 2
an = [xe, ye]
print(xe, ye, mins)
T = 0.0001
while True:
    xe += dx * T
    ye += dy * T
    # xe += dx
    # ye += dy
    temp = (xs - xe) ** 2 + (ys - ye) ** 2
    if temp >= mins:
        break
    # print(xe, ye, temp)
    an = [xe, ye]

    mins = temp
    T += 0.0001
for i in range(2):
    if an[i] - int(an[i]) > 0.5:
        an[i] = int(an[i]) + 1
    else:
        an[i] = int(an[i])
print(an)
