inputA, inputB, inputC = map(int, input().split())

print((inputA + inputB) % inputC)
print(((inputA % inputC) + (inputB % inputC)) % inputC)
print((inputA * inputB) % inputC)
print(((inputA % inputC) * (inputB % inputC)) % inputC)
