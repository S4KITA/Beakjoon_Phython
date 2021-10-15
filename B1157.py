word = input()
word = word.upper()
Alphabet = {}

for i in word:
    if i in Alphabet:
        Alphabet[i] += 1
    else:
        Alphabet[i] = 1

result = 0
temp = 0

for i in Alphabet:
    if Alphabet[i] > temp:
        temp = Alphabet[i]
        result = i
    elif Alphabet[i] == temp:
        result = '?'

print(result)