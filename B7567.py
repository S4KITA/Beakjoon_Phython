N = str(input())
mList = list(N)
height = 0

for i in range(len(mList)):
    if i == 0:
        temp = mList[i]
        height += 10
    else:
        if temp == mList[i]:
            height += 5
            temp = mList[i]
        else:
            height += 10
            temp = mList[i]

print(height)