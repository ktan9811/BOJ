a, b = map(int, input().split())
chessboard = [input() for _ in range(a)]
res = []
for i in range(a - 8 + 1):
    for j in range(b - 8 + 1):
        cnt1, cnt2 = 0,0
        for index in range(8*8):
            row = int(index/8) + i
            col = index%8 + j

            if (index + row) % 2 == 0:
                if chessboard[row][col] == 'B':
                    cnt1 += 1
                elif chessboard[row][col] == 'W':
                    cnt2 += 1
            else :
                if chessboard[row][col] == 'W':
                    cnt1 += 1
                elif chessboard[row][col] == 'B':
                    cnt2 += 1

        res.append(min(cnt1,cnt2))

res.sort()
print(res[0])