T = int(input())
for _ in range(T):
    R, S = input().split(' ')
    R = int(R)
    for ch in S:
        for _ in range(R):
            print(ch, end='')
    print()