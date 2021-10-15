inputA, inputB, inputC = map(int, input().split())

if(inputB >= inputC):
    print(-1)
else:
    print(int(inputA / (inputC - inputB)) + 1)