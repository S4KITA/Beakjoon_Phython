import sys

N = int(input())

mList = [0] * 10001

for i in range(N):
    mInputNum = int(sys.stdin.readline())
    mList[mInputNum] = mList[mInputNum] + 1

for j in range(10001):
    if mList[j] != 0:
        for k in range(mList[j]):
            print(j)
