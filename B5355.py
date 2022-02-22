N = int(input())
mList = []

for n in range(N):
    mList = list(map(str, input().split()))
    result = 0
    for i in range(len(mList)):
        if i == 0:
            result = float(mList[0])
        else:
            if mList[i] == '@':
                result = result * 3
            elif mList[i] == '%':
                result = result + 5
            elif mList[i] == '#':
                result = result - 7

    print("%0.2F" % result)
