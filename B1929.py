def IS_PRIME(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


inputA, inputB = map(int, input().split())

for n in range(inputA, inputB + 1):
    if IS_PRIME(n):
        print(n)
