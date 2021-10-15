inputA, inputB = input().split()
inputA = int(inputA[::-1])
inputB = int(inputB[::-1])

if inputA > inputB:
    print(inputA)
else:
    print(inputB)
