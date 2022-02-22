A, B, C = map(int, input().split())
mList = [A, B, C]
mListCount = [0, 0, 0, 0, 0, 0]

for i in range(6):
    mListCount[i] = mList.count(i + 1)

if max(mListCount) == 1:
    print(max(mList) * 100)
elif max(mListCount) == 2:
    print(1000 + (mListCount.index(max(mListCount)) + 1) * 100)
elif max(mListCount) == 3:
    print(10000 + (mListCount.index(max(mListCount)) + 1) * 1000)
