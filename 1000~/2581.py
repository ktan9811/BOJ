a = int(input())
b = int(input())

res = []
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
        res.append(i)
if len(res):
    print(sum(res))
    print(res[0])
else:
    print('-1')