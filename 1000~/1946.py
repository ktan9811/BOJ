T = int(input())
for _ in range(T):
    N = int(input())
    l = []
    for _ in range(N):
        a, b = map(int, input().split(' '))
        l.append((a,b))
    l.sort()
    res = []
    score = float("inf")
    for i in range(len(l)):
        if l[i][1] > score :
            continue
        else:
            res.append(l[i])
            score = l[i][1]

    print(len(res))
