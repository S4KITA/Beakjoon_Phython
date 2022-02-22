pq, K = map(int, input().split())

prime = [False, False] + [True] * (K - 2)
for i in range(2, int(K ** 0.5) + 1):
    if prime[i] == True:
        for j in range(i + 1, K, i):
            if prime[j] == True:
                prime[j] == False

result = True

for k in range(2, K):
    if prime[k] == True:
        if pq % k == 0:
            result = False
            break

if result == True:
    print('GOOD')
else:
    print('BAD', k)
