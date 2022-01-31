from sys import stdin, stdout

N = int(stdin.readline())
L = [0 for _ in range(8001)]

MIN, MAX = 4000, - 4000
for _ in range(N):
    cin = int(stdin.readline())
    if MIN > cin:
        MIN = cin
    if MAX < cin:
        MAX = cin
    L[cin] += 1

sum, cnt, MANY, mid = 0, 0, [(0, 0)], []

for i in range(MIN,MAX+1):
    if L[i] == 0:
        continue
    sum += i * L[i]
    cnt += L[i]
    if cnt > N//2:
        mid.append(i)

    if L[i] == MANY[0][1]:
        MANY.append((i,L[i]))
    elif L[i] > MANY[0][1]:
        MANY = [(i,L[i])]

flag = 0
if len(MANY) > 1:
    flag = 1
stdout.write(f"{round(sum / N)}\n{mid[0]}\n{MANY[flag][0]}\n{MAX - MIN}")