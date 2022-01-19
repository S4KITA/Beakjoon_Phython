import sys

N = int(input())
mList = []

for n in range(N):
    mList.append(sys.stdin.readline().strip())

mList = list(set(mList))
mList.sort(key=lambda x: (len(x), x))


for i in mList:
    print(i)
