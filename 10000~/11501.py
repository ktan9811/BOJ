T = int(input())
for _ in range(T):
    N = int(input())
    PL = list(map(int, input().split(' ')))
    res = 0
    MAX = 0
    for i in range(N):
        if PL[N-1-i] >= MAX:
            MAX = PL[N-1-i]
        else:
            res += MAX - PL[N-1-i]
    print(res)