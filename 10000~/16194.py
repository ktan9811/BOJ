N = int(input())
pricel = list(map(int, input().split(' ')))
dp = [0 for _ in range(N+1)]

for i in range(1,len(dp)):
    min = 10001
    for j in range(len(pricel)):
        if j + 1 > i: break
        else:
            if(dp[i-j-1] + pricel[j] < min):
                min = dp[i-j-1] + pricel[j]
    dp[i] = min
print(dp.pop())
