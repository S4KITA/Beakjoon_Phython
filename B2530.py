HH, MM, SS = map(int, input().split())
Times = int(input())

SS += Times % 60
Times = Times // 60
if SS >= 60:
    SS -= 60
    MM += 1

MM += Times % 60
Times = Times // 60

if MM >= 60:
    MM -= 60
    HH += 1

HH += Times % 24

if HH >= 24:
    HH -= 24

print(HH, MM, SS)
