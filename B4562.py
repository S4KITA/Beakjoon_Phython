N = int(input())

for n in range(N):
    X, Y = map(int, input().split())
    if X >= Y:
        print('MMM BRAINS')
    else:
        print('NO BRAINS')