import sys

input = sys.stdin.readline

N = int(input())
mList = []

for n in range(N):
    x, y = map(int, input().split())
    mList.append([x, y])

mList.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(mList[i][0], mList[i][1])
