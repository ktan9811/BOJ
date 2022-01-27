S = list(input().split(' '))
i=0

if S[0] == '':
    i += 1
if S[len(S)-1] == '':
    S.pop()
print(len(S[i:]))