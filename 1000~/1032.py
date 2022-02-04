N = int(input())
SL = [input() for _ in range(N)]
res = ''

for i in range(len(SL[0])):
    temp = SL[0][i]
    for str in SL:
        if str[i] != temp:
            temp = '?'
    res += temp
print(res)