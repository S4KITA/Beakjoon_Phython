def Kaprekar(n):
    a = 0
    for s in list(str(n)):
        a = a + int(s)
    return int(n) + a


able = []

for i in range(1, 10001):
    num = Kaprekar(i)
    able.append(num)

for j in range(1, 10001):
    if j in able:
        pass
    else:
        print(j)
