import sys

T = int(sys.stdin.readline())

for t in range(T):
    case = list(sys.stdin.readline())
    isVPS = False

    countVPS = 0

    for c in case:
        if countVPS >= 0:
            if c == '(':
                countVPS += 1
            elif c == ')':
                countVPS -= 1
        else:
            break

    if countVPS < 0:
        isVPS = False
    elif countVPS == 0:
        isVPS = True

    if isVPS:
        print('YES')
    else:
        print('NO')
