T = int(input())

for t in range(T):
    N, D = map(int, input().split())
    count = 0
    for n in range(N):
        v, f, c = map(int, input().split())
        if v * (f / c) >= D:
            count += 1
    print(count)
