N = int(input())
head = [2,3,5,7]
tail = [1,3,7,9]
def IsPrime(num):
    if num == 1:
        return False
    for i in range(2,int(num**(1/2)+1)):
        if num % i == 0:
            return False
    return True

def dfs(num):
    if 10**(N-1) < num and num < 10**(N):
        print(num)
    else:
        for t in tail:
            if(IsPrime(num*10 + t)):
                dfs(num*10 + t)

for h in head:
    dfs(h)


