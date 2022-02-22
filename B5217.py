T = int(input())

for t in range(T):
    cnt = 1
    N = int(input())

    print('Pairs for %d:' % N, end=' ')

    for i in range((N - 1) // 2):
        if i != 0:
            print(', ', end='')
        print(cnt, N - cnt, end='')
        cnt += 1
    print()
