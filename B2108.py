import sys
from collections import Counter

N = int(sys.stdin.readline())
mList = []
for n in range(N):
    mList.append(int(sys.stdin.readline()))

print(round(sum(mList) / N))

mList.sort()
print(mList[N // 2])

mListCount = Counter(mList).most_common()
if len(mListCount) > 1 and mListCount[0][1] == mListCount[1][1]:
    print(mListCount[1][0])
else:
    print(mListCount[0][0])

print(max(mList) - min(mList))
