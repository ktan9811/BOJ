N = int(input())
L = []
for _ in range(N):
    L.append(int(input()))

L.sort(reverse=True)
for item in L:
    print(item)