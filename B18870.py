import sys

input = sys.stdin.readline

N = int(input())
mList = list(map(int, input().split()))

mListIndex = sorted(list(set(mList)))
dic = {mListIndex[i]: i for i in range(len(mListIndex))}
for i in mList:
    print(dic[i], end=' ')
