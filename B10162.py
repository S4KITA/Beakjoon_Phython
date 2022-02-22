N = int(input())
A, B, C = 0, 0, 0

while True:
    if N - 300 >= 0:
        N = N - 300
        A += 1
    else:
        break

while True:
    if N - 60 >= 0:
        N = N - 60
        B += 1
    else:
        break

while True:
    if N - 10 >= 0:
        N = N - 10
        C += 1
    else:
        break

if N == 0:
    print(A, B, C)
else:
    print(-1)
