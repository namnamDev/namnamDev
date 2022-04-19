def binary(start, end):
    if start == end:
        return True
    mid = (start + end) // 2
    for i in range((end - start) // 2):
        if a[start + i] == a[end - i]:
            return False
    return binary(start, mid - 1) and binary(mid + 1, end)


for tc in range(int(input())):
    a = input()
    if binary(0, len(a) - 1):
        print("YES")
    else:
        print("NO")