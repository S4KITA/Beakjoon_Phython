mListDwarf = []
for i in range(9):
    mListDwarf.append(int(input()))

for i in range(9):
    for j in range(i + 1, 9):
        if 100 == sum(mListDwarf) - (mListDwarf[i] + mListDwarf[j]):
            DwarfA, DwarfB = mListDwarf[i], mListDwarf[j]

            mListDwarf.remove(DwarfA)
            mListDwarf.remove(DwarfB)
            mListDwarf.sort()  # 오름차순 정리

            for i in range(len(mListDwarf)):
                print(mListDwarf[i])
            break

    if len(mListDwarf) < 9:
        break
