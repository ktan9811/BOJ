omok = [[0 for _ in range(19)] for _ in range(19)]
print (omok[18])
N = int(input())
act = []

res = -1

for n in range(N):
    i,j = map(int, input().split(' '))
    act.append((i-1,j-1))
print(act)

def check1(i,j):
    bi, bj= i, j
    base = omok[i][j]
    cnt = 0
    while i < 18:
        i += 1
        if omok[i][j] == base:
            cnt += 1
        else :
            break
    i, j = bi, bj
    while 0 < i:
        i -= 1
        if omok[i][j] == base:
            cnt += 1
        else :
            break
    print('1:',cnt)
    if cnt == 4:
        return True
    else :
        return False

def check2(i,j):
    bi, bj= i, j
    base = omok[i][j]
    cnt = 0
    while j < 18:
        j += 1
        if omok[i][j] == base:
            cnt += 1
        else :
            break
    i, j = bi, bj
    while 0 < j:
        j -= 1
        if omok[i][j] == base:
            cnt += 1
        else :
            break
    print('2:',cnt)
    if cnt == 4:
        return True
    else :
        return False
        

def check3(i,j):
    bi, bj= i, j
    base = omok[i][j]
    cnt = 0
    while i < 18 and j < 18:
        i += 1
        j += 1
        if omok[i][j] == base:
            cnt += 1
        else :
            break
    i, j = bi, bj
    while 0 < i and 0 < j:
        i -= 1
        j -= 1
        if omok[i][j] == base:
            cnt += 1
        else :
            break
    print('3:',cnt)
    if cnt == 4:
        return True
    else :
        return False

for n in range(len(act)):
    if n % 2 == 0: omok[act[n][0]][act[n][1]] = 1
    else : omok[act[n][0]][act[n][1]] = 2
    if check1(act[n][0],act[n][1]) or check2(act[n][0],act[n][1]) or check3(act[n][0],act[n][1]):
        res = n + 1
        break
    print(act[n])
    print('-------------------')

print(res)