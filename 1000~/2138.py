N = int(input())
IN1 = input()
IN2 = input()

SRC = []
SRC2 = []
DST = []

for i in range(N):
    SRC.append(int(IN1[i]))
    SRC2.append(int(IN1[i]))
    DST.append(int(IN2[i]))

cnt = 0
cnt2 = 1

SRC2[0] ^= 1
SRC2[1] ^= 1

for i in range(1,N):
    if SRC[i-1] != DST[i-1]:
        cnt += 1
        SRC[i-1] ^= 1
        SRC[i] ^= 1
        if i < N-1 : SRC[i+1] ^= 1
    if SRC2[i-1] != DST[i-1]:
        cnt2 += 1
        SRC2[i-1] ^= 1
        SRC2[i] ^= 1
        if i < N-1 : SRC2[i+1] ^= 1

if SRC == DST: print(cnt)
elif SRC2 == DST: print(cnt2)
else: print(-1)