T = int(input())
for _ in range(T):
    S, E = map(int, input().split(' '))
    dist = E - S
    n = 0

    while(True):
        n += 1
        if n % 2 == 1:
            if dist <= (n//2 + 1) ** 2:
                break
        else :
            if dist <= (n//2) * (n//2+1):
                break
    print(n)
