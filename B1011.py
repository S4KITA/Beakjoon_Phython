inputA = int(input())

for a in range(inputA):
    x, y = map(int, input().split())
    Space = y - x
    Count = 0
    Moveable = 1
    Distance = 0
    while Distance < Space:
        Count += 1
        Distance += Moveable
        if Count % 2 == 0:
            Moveable += 1
    print(Count)
