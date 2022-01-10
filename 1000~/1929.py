a, b = input().split(' ')
a = int(a)
b = int(b)
for i in range(a,b+1):
    if i == 1:
        continue
    flag = True
    b = int(i**(1/2))
    for j in range(2,b+1):
        if i % j == 0:
            flag = False
            break
    if(flag):
        print(i)
