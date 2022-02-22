Result = 0

for i in range(5):
    N = int(input())
    if N < 40:
        N = 40
    Result += N

print(int(Result / 5))
