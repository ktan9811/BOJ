S = input()
AL = [[0,chr(ord('A')+i)] for i in range(26)]
for ch in (S):
    if 'A' <= ch and ch <= 'Z':
        AL[ord(ch) - ord('A')][0] += 1
    else:
        AL[ord(ch) - ord('a')][0] += 1

AL.sort(reverse=True)
if AL[0][0] == AL[1][0]:
    print('?')
else:
    print(AL[0][1])
