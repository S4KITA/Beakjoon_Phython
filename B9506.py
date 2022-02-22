while True:
    N = int(input())

    if N == -1:
        break

    mListDivisor = []
    for n in range(1, N):
        if N % n == 0:
            mListDivisor.append(n)
    if N == sum(mListDivisor):
        print(N, " = ", " + ".join(str(i) for i in mListDivisor), sep="")
    else:
        print(N, 'is NOT perfect.')
