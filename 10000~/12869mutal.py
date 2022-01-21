a = int(input())
b = list(map(int, input().split( )))

while(len(b) < 3):
    b.append(0)

dp = [[[-1 for _ in range(61)]for _ in range(61)]for _ in range(61)]

dp[0][0][0] = 0
attack = [(9,3,1),(9,1,3),(3,9,1),(3,1,9),(1,9,3),(1,3,9)]

def mutal(x,y,z):
    if dp[x][y][z] != -1:
        return dp[x][y][z]

    else: 
        dp[x][y][z] = 10000
        for at in attack:
            dp[x][y][z] = min(dp[x][y][z], mutal(max(0,x-at[0]),max(0,y-at[1]),max(0,z-at[2]))+1)
        return dp[x][y][z]

print(mutal(b[0],b[1],b[2]))