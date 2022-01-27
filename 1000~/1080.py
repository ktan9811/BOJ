N, M = map(int, input().split(' '))
SL = [list(input()) for _ in range(N)]
RL = [list(input()) for _ in range(N)]


for i in range(N):
    for j in range(M):
        SL[i][j] = int(SL[i][j])
        RL[i][j] = int(RL[i][j])

cnt = 0
for i in range(1,N-1):
    for j in range(1,M-1):
        if SL[i-1][j-1] != RL[i-1][j-1]:
            cnt += 1
            for x in range(-1,2):
                for y in range(-1,2):
                    SL[i+x][j+y] ^= 1 
if SL == RL:
    print(cnt)
else:
    print(-1)