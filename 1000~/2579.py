N = int(input())
STEP = [int(input()) for _ in range(N)]
dp = [0 for _ in range(N)]
dp[0] = STEP[0]
if(N >= 2): dp[1] = STEP[0] + STEP[1]
if(N >= 3): dp[2] = STEP[2] + max(STEP[0], STEP[1])
for i in range(3,N):
    dp[i] = STEP[i] + max(dp[i-2],dp[i-3] + STEP[i-1])
print(dp.pop())