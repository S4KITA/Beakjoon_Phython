inputA = int(input())

for i in range(inputA):
    H, W, N = map(int, input().split())
    Room = N // H + 1
    Floor = N % H
    if N % H == 0:  # h의 배수이면,
        Room = N // H
        Floor = H
    print(f'{Floor * 100 + Room}')
