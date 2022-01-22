S = input()

cnt0 = 0
cnt1 = 0
i = -1
print(len(S))
while(i < len(S) - 1):
    i += 1
    if S[i] == '1':
        cnt0 += 1
        while(i < len(S) and S[i] == '1'):
            i += 1

i = -1
while(i < len(S) - 1):
    i += 1
    if S[i] == '0':
        cnt1 += 1
        while(i < len(S) and S[i] == '0'):
            i += 1

print(min(cnt0,cnt1))