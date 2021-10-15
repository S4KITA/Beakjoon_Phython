T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    people = [p for p in range(1, n + 1)]
    for j in range(k):
        for k in range(1, n):
            people[k] += people[k - 1]
    print(people[-1])
