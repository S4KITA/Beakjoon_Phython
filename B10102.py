N = int(input())
mList = list(str(input()))
countA, countB = 0, 0

for n in range(len(mList)):
    if mList[n] == 'A':
        countA += 1
    elif mList[n] == 'B':
        countB += 1

if countA > countB:
    print('A')
elif countA == countB:
    print('Tie')
else:
    print('B')
