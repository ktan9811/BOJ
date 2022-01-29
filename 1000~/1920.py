import sys

def bisect(SL, target):
    start = 0
    end = len(SL) - 1
    while(start <= end):
        mid = (start + end) // 2
        if target > SL[mid]:
            start = mid + 1
        elif target < SL[mid]:
            end = mid - 1
        else:
            return 1
    return 0

sys.stdin.readline()
SL = list(map(int, sys.stdin.readline().split(' ')))
sys.stdin.readline()
NL = list(map(int, sys.stdin.readline().split(' ')))
SL.sort()
for num in NL:
    sys.stdout.write(f"{bisect(SL, num)}\n")