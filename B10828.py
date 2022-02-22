import sys

N = int(sys.stdin.readline())
Stack = []

for n in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        Stack.append(command[1])
    elif command[0] == 'pop':
        if len(Stack) == 0:
            print(-1)
        else:
            print(Stack.pop())
    elif command[0] == 'size':
        print(len(Stack))
    elif command[0] == 'empty':
        if len(Stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(Stack) == 0:
            print(-1)
        else:
            print(Stack[-1])
