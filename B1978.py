inputA = int(input())
number = map(int, input().split())

prime_number = 0

for n in number:
    count = 0
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                count += 1
        if count == 0:
            prime_number += 1

print(prime_number)