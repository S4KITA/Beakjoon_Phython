N = int(input())
listCatalog = []
isTrue = True
count = 0

for n in range(N):
    listCatalog.append(int(input()))

for i in listCatalog:
    for x in range(1, int(i // 2)):
        for y in range(1, int(i // 2)):
            if i == (2 * (x * y) + x + y):
                break

print(count)
