import math


def IS_PRIME(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True


mListPrime = []

for i in range(2, 246912):
    if IS_PRIME(i):
        mListPrime.append(i)

while True:
    count = 0

    InputA = int(input())

    if InputA == 0:
        break

    for num in mListPrime:
        if InputA < num <= InputA * 2:
            count += 1

    print(count)
