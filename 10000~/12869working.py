a = int(input())
b = list(map(int, input().split( )))
cnt = 0
b.sort(reverse=True)
while(len(b)):
    if len(b) == 3:
        b[0] -= 9
        b[1] -= 3
        b[2] -= 1
    elif len(b) == 2:
        b[0] -= 9
        b[1] -= 3
    elif len(b) == 1:
        b[0] -= 9
    cnt += 1
    b.sort(reverse=True)
    if b[0] <= 0:
        break
print(cnt)
