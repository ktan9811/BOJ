T = int(input())
for _ in range(T):
    S = input()
    res = 0
    cnt = 0
    for ch in S:
        if ch == 'O':
            cnt += 1
            res += cnt
        else:
            cnt = 0
    print(res)