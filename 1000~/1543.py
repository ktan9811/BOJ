S = input()
I = input()

i = 0
cnt = 0
while(i < len(S)):
    if S[i:i+len(I)] == I:
        i += len(I)
        cnt += 1
    else:
        i += 1
print(cnt)