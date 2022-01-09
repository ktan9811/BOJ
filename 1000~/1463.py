a = int(input())
dp = [0 for _ in range(10**6+1)]
if a <= 3:
    print(1)
    quit()

dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(4,a+1):
    min1, min2, min3 = 10**6, 10**6, 10**6
    min1 = dp[i-1] + 1
    if i % 2 == 0:
        min2 = dp[i//2] + 1
    if i % 3 == 0:
        min3 = dp[i//3] + 1
    dp[i] = min(min1,min2,min3)

print(dp[i])