N, M = map(int, input().split())
mList = []
mListMin = []

for i in range(N):
    Pattern = input()
    mList.append(Pattern)

for i in range(N - 7):
    for j in range(M - 7):
        numA = 0
        numB = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if mList[a][b] != 'W':
                        numA += 1
                    else:
                        numB += 1
                else:
                    if mList[a][b] != 'B':
                        numA += 1
                    else:
                        numB += 1
        mListMin.append(numA)
        mListMin.append(numB)

print(min(mListMin))
