inputA = int(input())
for i in range(inputA):
    inputB, inputC = input().split()
    for j in inputC:
        print(j * int(inputB), end = '')
    print()
