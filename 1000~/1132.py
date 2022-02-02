N = int(input())
L = [input() for _ in range(N)]
AL = [0 for _ in range(10)]
AD = {'A': 0, 'B' : 0, 'C': 0, 'D' : 0, 'E': 0, 'F' : 0, 'G': 0, 'H' : 0, 'I': 0, 'J' : 0}
CanZero = {'A': True, 'B' : True, 'C': True, 'D' : True, 'E': True, 'F' : True, 'G': True, 'H' : True, 'I': True, 'J' : True}
for str in L:
    length = len(str)
    CanZero[str[0]] = False
    for i in range(length):
        AD[str[length - i - 1]] += 10**i

SD = sorted(AD.items(), key = lambda x : x[1], reverse=True)

if not CanZero[SD[9][0]]:
    i = 9
    while(not CanZero[SD[i][0]]):
        i -= 1
    temp = SD[i]
    del SD[i]
    SD.append(temp)


res = 0
for i in range(9):
    res += SD[i][1] * (9-i)
print(res)