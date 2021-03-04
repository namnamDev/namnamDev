H, M = map(int, input().split())
if M < 45:
    if H == 0:
        H = 24 - 1
    else:
        H = H - 1
    M = 45 - M
else:
    M = M - 45

print("{} {}".format(H, M))
