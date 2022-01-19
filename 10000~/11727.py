a = int(input())
dp = [0 for _ in range(1000+1)]
dp[2] = 3
dp[3] = 5
for i in range(4,a+1):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[a]%10007)