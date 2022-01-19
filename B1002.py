T = int(input())

for t in range(T):
    X1, Y1, R1, X2, Y2, R2 = map(int, input().split())
    distance = (((X1 - X2) ** 2) + ((Y1 - Y2) ** 2)) ** 0.5

    if distance == 0 and R1 == R2:
        print(-1)
    elif abs(R1 - R2) == distance or R1 + R2 == distance:
        print(1)
    elif abs(R1 - R2) < distance < R1 + R2:
        print(2)
    else:
        print(0)
