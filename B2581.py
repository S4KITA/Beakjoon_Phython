inputA = int(input())
inputB = int(input())
number = []

prime = True

for n in range(inputA, inputB + 1):
    if n == 1:
        prime = False

    for i in range(2, n):
        if n == 2:
            number.append(n)
            break
        else:
            if n % i == 0:
                prime = False
                break

    if prime == True:
        number.append(n)
    else:
        prime = True

if len(number) == 0:
    print(-1)
else:
    print(sum(number))
    print(min(number))
