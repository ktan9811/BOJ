N = int(input())
lst = []
for i in range(N):
    a, b = map(int, input().split(' '))
    lst.append((a,b))
lst.sort(key = lambda x : (x[1], x[0]))

start = 0
cnt = 0
for i in range(len(lst)):
    if lst[i][0] >= start:
        cnt += 1
        start = lst[i][1]
print(cnt)