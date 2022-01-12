n = int(input())
m = [list(map(int, input().split(' '))) for _ in range(n)]
dm = m

for i in range(len(m)):
    for j in range(len(m)):
        if m[i][j] == 1:
            dm[i][j] = float('inf')


index = 0
while(index != n - 1):
    index += 1
    if not m[0][index] : dm[0][index] =  dm[0][index-1] + 1
    if not m[index][0] : dm[index][0] =  dm[index-1][0] + 1

    for i in range(1,index-1):
        if not m[i][index]:
            dm[i][index] =  min(dm[i-1][index],dm[i-1][index-1],dm[i][index-1]) + 1
    for i in range(1,index):
        print(index, i, min(dm[i-1][index],dm[i-1][index-1],dm[i][index-1]) + 1)
        if not m[index][i]:
            dm[index][i] =  min(dm[i-1][index],dm[i-1][index-1],dm[i][index-1]) + 1
print(dm)