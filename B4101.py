while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    if (N > M):
        print("Yes")
    else:
        print("No")
