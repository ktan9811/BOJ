a, b = map(int, input().split(' '))
sqmap = [input() for _ in range(a)]
max = 1
for i in range(a):
    for j in range(b):
        for k in range(1,a):
            if i+k >= a or j+k >= b:
                break
            print(i,j,k)
            print(sqmap[i][j],sqmap[i+k][j+k])
            if sqmap[i][j] == sqmap[i+k][j] == sqmap[i+k][j+k] == sqmap[i][j+k]:
                if k >= max:
                    max = k + 1
print(max**2)