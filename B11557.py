T = int(input())

for t in range(T):
    N = int(input())
    mList = []

    for n in range(N):
        Name, Alcohol = map(str, input().split())
        mList.append([Name, int(Alcohol)])

    mList = sorted(mList, key=lambda x: x[1])

    print(mList[-1][0])
