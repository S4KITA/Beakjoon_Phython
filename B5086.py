while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    if N > M and N % M == 0:
        print("multiple")
    elif N < M and M % N == 0:
        print("factor")
    else:
        print('neither')
