dp = [0 for _ in range(1000+1)]
dp[1] = 1
dp[2] = 2
for i in range(3,1000+1):
    dp[i] = dp[i-1] + dp[i-2]

a = int(input())
print(dp[a]%10007)