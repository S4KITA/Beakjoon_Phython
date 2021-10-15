inputA = int(input())
num = 2

while inputA != 1:
    if inputA % num == 0:
        inputA = inputA / num
        print(num)
    else:
        num += 1