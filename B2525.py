HH, MM = map(int, input().split())
Times = int(input())

MM_Result = MM + Times

if MM_Result >= 60:
    MM_Result = int(MM_Result % 60)

HH_Result = HH + int((MM + Times) / 60)

if HH_Result >= 24:
    HH_Result = HH_Result - 24

print(HH_Result, MM_Result)
