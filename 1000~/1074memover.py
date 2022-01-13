N, r, c = map(int, input().split(' '))
zmap = [[0 for _ in range(2**N)] for _ in range(2**N)]
zmap[r][c] = 1

def zsearch(n,i,j,cnt=0):
    if n < 0 :
        return
    elif zmap[i][j] == 1:
        print('cnt : ',cnt)
        quit()
    else:
        n = n - 1
        search = 2**(n)     #2
        zsearch(n,i,j,cnt)
        zsearch(n,i,j+search,cnt+search**2)         #4
        zsearch(n,i+search,j,cnt+2*search**2)       #8
        zsearch(n,i+search,j+search,cnt+3*search**2)#12

zsearch(N,0,0)