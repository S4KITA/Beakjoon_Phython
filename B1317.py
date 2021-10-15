inputA = int(input())
result = inputA
for i in range(0, inputA):
    inputB = input()
    for j in range(0, len(inputB) - 1):
        if inputB[j] == inputB[j + 1]:
            pass
        elif inputB[j] in inputB[j + 1:]:
            result -= 1
            break
print(result)
