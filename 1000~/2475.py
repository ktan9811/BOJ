NL = list(map(int, input().split(' ')))

res = 0
for num in NL:
    res += num ** 2
    res %= 10

print(res)