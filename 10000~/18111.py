from sys import stdin, stdout

I, J, N = map(int, stdin.readline().split(' '))

MIN = 256
MAX = 0

NL = [0 for _ in range(257)]
for _ in range(I):
    TL = list(map(int, stdin.readline().split(' ')))
    for num in TL:
        if num <= MIN:
            MIN = num
        if num >= MAX:
            MAX = num
        NL[num] += 1

res = []
for n in range(MIN, MAX + 1):
    goal = n
    block = N
    time = 0
    for i in range(MIN, MAX +1):
        if NL[i] == 0:
            continue
        if i > goal:
            time += (i - goal) * NL[i] * 2
        elif i < goal:
            time += (goal - i) * NL[i]
        block += (i - goal) * NL[i]
    if block >= 0:
        res.append((time, goal))

res.sort(key = lambda x:(x[0], -x[1]))
stdout.write(f"{res[0][0]} {res[0][1]}")