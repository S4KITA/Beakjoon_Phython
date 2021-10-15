alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
inputA = str(input())

for i in alphabet:
    inputA = inputA.replace(i, 'X')

print(len(inputA))