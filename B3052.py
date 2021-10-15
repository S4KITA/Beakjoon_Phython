arrayA = []
arrayB = []
for i in range(10):
    arrayA.append(int(input()))

for i in range(10):
    arrayB.append(arrayA[i] % 42)

arrayB = set(arrayB)
print(len(arrayB))
