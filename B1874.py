N = int(input())
stack = []
result = []
count = 0
isPossible = True

for n in range(N):
    num = int(input())

    while count < num:
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        isPossible = False
        break

if isPossible == False:
    print('NO')
else:
    for i in result:
        print(i)
