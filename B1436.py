N = int(input())
count = 0
numSix = 666

while True:
    if '666' in str(numSix):
        count += 1
    if count == N:
        print(numSix)
        break

    numSix += 1
