trial = int(input())
a = list(map(int, (input().split(' '))))
cnt = 0
for i in a:
    if i == 1:
        continue
    flag = True
    b = int(i**(1/2))
    for j in range(2,b+1):
        if i % j == 0:
            flag = False
            break
    if(flag):
        cnt += 1
print(cnt)