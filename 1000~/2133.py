a = int(input())
dp = [0 for _ in range(30+1)]

dp[0] = 1
dp[2] = 3

for i in range(4,31,2):
    dp[i] = dp[i-2] * 3
    for j in range(0,i-4+1,2):
        dp[i] = dp[i] + dp[j] * 2

print(dp[a])