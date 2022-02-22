N = int(input())
mListScore = [0] * N

for n in range(N):
    A, B, C = map(int, input().split())
    mList = [A, B, C]
    mListCount = [0, 0, 0, 0, 0, 0]

    score = 0

    for i in range(6):
        mListCount[i] = mList.count(i + 1)

    if max(mListCount) == 1:
        score = max(mList) * 100
    elif max(mListCount) == 2:
        score = 1000 + (mListCount.index(max(mListCount)) + 1) * 100
    elif max(mListCount) == 3:
        score = 10000 + (mListCount.index(max(mListCount)) + 1) * 1000

    mListScore[n] = score

print(max(mListScore))
