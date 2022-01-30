from sys import stdin, stdout
K = int(stdin.readline())
res = []
for _ in range(K):
    temp = int(stdin.readline())
    if temp == 0:
        res.pop()
    else:
        res.append(temp)
stdout.write(f"{sum(res)}")