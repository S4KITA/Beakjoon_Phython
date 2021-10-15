arrayA = []
for i in range(9):
    arrayA.append(int(input()))

print(max(arrayA))
print(arrayA.index(max(arrayA)) + 1)
