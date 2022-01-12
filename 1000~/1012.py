def eat(i,j):
    if farm[i][j] != 1:
        return
    else:
        farm[i][j] = 7
        if i < M - 1 and farm[i+1][j] == 1: eat(i+1,j)
        if i > 0 and farm[i-1][j] == 1: eat(i-1,j)
        if j < N - 1 and farm[i][j+1] == 1: eat(i,j+1)
        if j > 0 and farm[i][j-1] == 1: eat(i,j-1)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split(' '))
    farm = [[0 for _ in range(N)]for _ in range(M)]
    cnt = 0

    for _ in range(K):
        m, n = map(int, input().split(' '))
        farm[m][n] = 1

    for i in range(M):
        for j in range(N):
            if farm[i][j] == 1:
                eat(i,j)
                cnt +=1
    print(cnt)