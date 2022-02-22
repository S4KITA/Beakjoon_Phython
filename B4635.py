while True:
    temp = 0
    distance = 0

    N = int(input())

    if N == -1:
        break

    for n in range(N):
        s, t = map(int, input().split())
        distance += s * (t - temp)
        temp = t

    print(distance, 'miles')
