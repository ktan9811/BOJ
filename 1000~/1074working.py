N, r, c = map(int, input().split(' '))
zmap = [[0 for _ in range(N**2)] for _ in range(N**2)]

def zsearch(n,i,j,cnt):
    if i == r and j == c:
        return
    