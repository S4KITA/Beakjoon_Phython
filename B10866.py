import sys
from collections import deque

N = int(sys.stdin.readline())
Deque = deque()

for n in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        Deque.appendleft(command[1])
    elif command[0] == 'push_back':
        Deque.append(command[1])
    elif command[0] == 'pop_front':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque.popleft())
    elif command[0] == 'pop_back':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque.pop())
    elif command[0] == 'size':
        print(len(Deque))
    elif command[0] == 'empty':
        if len(Deque) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[0])
    elif command[0] == 'back':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[len(Deque) - 1])
