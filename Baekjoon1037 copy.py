N = int(input())
yakList = list(map(int,input().split()))
yakList.sort(reverse=True)

print(yakList[0] *yakList[-1])
