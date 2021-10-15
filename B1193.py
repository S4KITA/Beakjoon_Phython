inputA = int(input())
num_list = []

number = 0
count = 0

while count < inputA:
    number += 1
    count += number

count -= number

if number % 2 == 0:
    x = inputA - count
    y = number - x + 1
else:
    x = number - (inputA - count) + 1
    y = inputA - count

print(f"{x}/{y}")
