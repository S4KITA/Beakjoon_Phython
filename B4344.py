inputA = int(input())

for i in range(inputA):
    mListA = list(map(int, input().split()))
    avg = sum(mListA[1:]) / mListA[0]
    count = 0
    for score in mListA[1:]:
        if score > avg:
            count += 1

        rate = count / mListA[0] * 100

    print(f"{rate:.3f}%")
