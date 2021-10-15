inputA = int(input())
ListA = list(map(int, input().split()))
Max = max(ListA)

ListB = []

for i in ListA:
    ListB.append(i / Max * 100)

Avg = sum(ListB) / inputA
print(Avg)
