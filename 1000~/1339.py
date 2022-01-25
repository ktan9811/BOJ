N = int(input())
WL = []
for _ in range(N):
    WL.append(input())

AL = [0 for _ in range(26)]

for an in WL:
    length = len(an)
    for i in range(length):
        AL[ord(an[length - i - 1]) - ord("A")] += 10**i

AL.sort(reverse=True)

res = 0
for i in range(10):
    res += AL[i] * (9 - i)
print(res)