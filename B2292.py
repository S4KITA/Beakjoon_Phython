inputA = int(input())

count = 1
Honeycomb = 1

while inputA > Honeycomb:
    Honeycomb += 6 * count
    count += 1

print(count)