N = int(input())
PL = []
for _ in range(N):
    PL.append(int(input()))

PL.sort()

res = 0

for i in range(len(PL)):
    res += abs(PL[i] - (i + 1))

print(res)