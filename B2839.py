inputA = int(input())

result = 0

while inputA >= 0:
    if inputA % 5 == 0:
        result += (inputA // 5)
        print(result)
        break
    inputA -= 3
    result += 1
else:
    print(-1)
