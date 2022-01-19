N = int(input())
mList = []

for n in range(N):
    mList.append(int(input()))

mList = sorted(mList)

for i in range(len(mList)):
    print(mList[i])