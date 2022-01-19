N = int(input())

result = 0

for n in range(1, N + 1):
    mList = list(map(int, str(n)))
    result = n + sum(mList)
    if result == N:
        print(n)
        break

    if n == N:
        print(0)
