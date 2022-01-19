N = int(input())
mList = []
rank = []

for n in range(N):
    X, Y = map(int, input().split())
    mList.append((X, Y))

for i in range(N):
    count = 0
    for j in range(N):
        if mList[i][0] < mList[j][0] and mList[i][1] < mList[j][1]:
            count += 1
    rank.append(count + 1)

for r in rank:
    print(r, end=" ")
