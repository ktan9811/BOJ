A = int(input())
B = int(input())
C = int(input())

NL = [0 for _ in range(10)]
mul = A * B * C

while (mul != 0):
    NL[mul % 10] += 1
    mul = mul // 10

for item in NL:
    print(item)
