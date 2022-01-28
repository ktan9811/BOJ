N = int(input())
L = []
for _ in range(N):
    L.append(int(input()))

L.sort()
for item in L:
    print(item)