inputA = int(input())
inputB = int(input())
inputC = int(input())

result = list(str(inputA * inputB * inputC))

for i in range(10):
    print(result.count(str(i)))
