N = int(input())
countO, countX = 0, 0;

for n in range(N):
    if int(input()) == 0:
        countX += 1
    else:
        countO += 1

if countO > countX:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')