N = int(input())
score = []
for _ in range(N):
    score.append(int(input()))

i = 1
cnt = 0
while(N-i-1 >= 0):
    if score[N - i] <= score[N - i - 1]:
        score[N - i - 1] -= 1
        cnt += 1
    else:
        i += 1

print(cnt)