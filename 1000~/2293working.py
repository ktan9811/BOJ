n, k = input().split(' ')
n, k = int(n), int(k)
coin = [int(input()) for _ in range(n)]
print(coin)
dp = [0 for _ in range(k)]
for c in coin:
    dp[c] = 1

for i in range (1,k):
    add = 0
    for c in coin:
        if(i < c):
            continue
        add += dp[i - c]
    dp[i] += add
print(dp)

# 1 3 == 10
# 1 = dp[1] + dp[0] + dp[0]
# 3 = dp[3] + dp[2] + dp[0
# 4 = dp[4] + dp[4-1] + dp[4-3] == dp(i-c = 가 나오면 동일한 case 존재)
# 5 = dp[5] + dp[5-1] + dp[5-3] == 4원 case + 2원 case 경우가  안겹침 
# 6 = dp[6] + dp[6-1] + dp[6-3] == 5 + 1 case / 3 + 3 case 경우가  안겹침 

# 3 + 1 =
# 1 + 3 =

# 4 + 1 = # 2 + 3