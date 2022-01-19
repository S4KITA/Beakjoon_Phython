import sys

input = sys.stdin.readline

N = int(input())
mList = []

for n in range(N):
    x, y = map(int, input().split())
    mList.append([y, x])

mList.sort(key=lambda x: (x[0], x[1]))

for y, x in mList:
    print(x, y)
