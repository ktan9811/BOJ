a, b = map(int, (input().split(' ')))
coins = []
for _ in range(a):
    coins.append(int(input()))
dp = [0 for _ in range(b+1)]
dp[b] = -1

for coin in coins:
    if coin <= b:
        dp[coin] = 1

for i in range(0,len(dp)):
    minl = []
    for coin in coins:
        if i-coin == 0:
            minl.append(1)
        elif coin <= i and dp[i-coin] != 0:
            minl.append(dp[i-coin]+1)
    if minl :
        dp[i] = min(minl)

print(dp)
print(dp[b])