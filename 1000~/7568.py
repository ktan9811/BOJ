a = int(input())
wh = [0 for _ in range(a)]
for i in range (a):
    wh[i] = list(map(int, input().split()))
res = []
for i in range (a):
    rate = 1
    for j in range(a):
        if wh[i][0] < wh[j][0] and wh[i][1] < wh[j][1] :
            rate += 1
    res.append(rate)
for item in res:
    print (item, end =' ')