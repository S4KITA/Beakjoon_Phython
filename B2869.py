import math

inputA, inputB, inputC = map(int, input().split())

print(int(math.ceil((inputC - inputA) / (inputA - inputB))) + 1)
