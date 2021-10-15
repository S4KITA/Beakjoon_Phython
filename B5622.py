dial = ['A B C', 'D E F', 'G H I', 'J K L', 'M N O', 'P Q R S', 'T U V', 'W X Y Z']

# 65부터 90 A to Z
inputA = list(str(input()))
count = 0

for i in inputA:
    if ord(i) >= 65 and ord(i) < 68:
        count += 3
    elif ord(i) >= 68 and ord(i) < 71:
        count += 4
    elif ord(i) >= 71 and ord(i) < 74:
        count += 5
    elif ord(i) >= 74 and ord(i) < 77:
        count += 6
    elif ord(i) >= 77 and ord(i) < 80:
        count += 7
    elif ord(i) >= 80 and ord(i) < 84:
        count += 8
    elif ord(i) >= 84 and ord(i) < 87:
        count += 9
    elif ord(i) >= 87 and ord(i) < 91:
        count += 10

print(count)
