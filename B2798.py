N, M = map(int, input().split())
numList = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if numList[i] + numList[j] + numList[k] > M:
                continue
            else:
                result = max(result, numList[i] + numList[j] + numList[k])

print(result)
