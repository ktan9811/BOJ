 #N point to M , How many Bridge can be made
 #can't be cross
def fact(n):
    res = 1
    for i in range(1,n+1):
        res = res * i
    return res


trial = int(input())
for _ in range(trial):
    n, m = input().split()
    n, m = int(n), int(m)
    print(fact(m)//fact(m-n)//fact(n))    #it does well