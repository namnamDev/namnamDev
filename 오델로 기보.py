gi = "f5d6c3d3c4b5b4f4c5b3f3c6b6e6a4a6a5f6e3g6g5a3d2h5c2g4e7f7g3h2c7e1c1e8d7f2e2f1h3h4d1b1h6h7g2d8c8b8b7g7f8a8a7g8h8h1g1a1a2b2"
cnt = 0
print(ord("a"))
cnt = 0
an = 1
for i in range(0, len(gi), 2):
    cnt += 1
    print(ord(gi[i]) - ord("a") + 1, gi[i + 1], an)
    an = 3 - an
print(cnt)
