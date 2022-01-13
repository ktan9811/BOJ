n = int(input())
nl = list(map(int, input().split(' ')))
dp = [float("-inf") for _ in range(n)]
dp[0] = nl[0]

for i in range(1,len(nl)):
    dp[i] = max(nl[i]+dp[i-1],nl[i])

print(max(dp))