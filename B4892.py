import sys

i = 1
while True:

    N0 = int(sys.stdin.readline())
    if N0 == 0:
        break
    else:
        N1 = N0 * 3
        if N1 % 2 == 0:
            N2 = int(N1 / 2)
        else:
            N2 = int((N1 + 1) / 2)
        N3 = 3 * N2
        N4 = int(N3 / 9)
    if N1 % 2 == 1:
        print("%d. odd %d" % (i, N4))
    else:
        print("%d. even %d" % (i, N4))
    i += 1
