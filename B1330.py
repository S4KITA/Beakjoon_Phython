inputA, inputB = map(int, input().split())

if inputA > inputB:
    print("<")
elif inputA < inputB:
    print(">")
else:
    print("==")
