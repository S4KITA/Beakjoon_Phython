mListPrime = [0 for i in range(10001)]
mListPrime[1] = 1
for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        mListPrime[j] = 1
T = int(input())

for i in range(T):
    num = int(input())
    temp = num // 2
    for j in range(temp, 1, -1):
        if mListPrime[num - j] == 0 and mListPrime[j] == 0:
            print(j, num - j)
            break
