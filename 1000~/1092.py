import sys
from bisect import *

input = sys.stdin.readline

n = int(input())
crain = list(map(int, input().split()))
k = int(input())
boxes = list(map(int, input().split()))

crain.sort(reverse=True)

boxes.sort()

if crain[0] < boxes[-1]:
    print(-1)
    exit()
    
cnt = 0
while boxes:
    cnt += 1
    for c in crain:
        right = bisect_right(boxes, c)
        if boxes and boxes[right-1] <= c:
            boxes.pop(right-1)

print(cnt)