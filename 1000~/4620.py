while(True):
    N = int(input())
    if N == -1:
        break
    M = list(input() for _ in range(N))
    res = 0
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if i == (N - 1) and j == (N - 1):
                break
            if dp[i][j] == 0:
                continue
            move = int(M[i][j])
            if i + move < N:
                dp[i+move][j] += dp[i][j]
            if j + move < N:
                dp[i][j+move] += dp[i][j]
    print(dp[N-1][N-1])
