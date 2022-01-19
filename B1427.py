N = int(input())
mList = []
for i in str(N):
    mList.append(int(i))

mList.sort()
mList.reverse()

for j in mList:
    print(j, end='')
