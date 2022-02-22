N, K = map(int, input().split())
listN = list(range(1, N + 1))

listAnswer = []
temp = 0

for n in range(N):
    temp += K - 1
    if temp > - len(listN):
        temp = temp % len(listN)

    listAnswer.append(str(listN.pop(temp)))

print('<', ', '.join(listAnswer)[:], '>', sep='')
