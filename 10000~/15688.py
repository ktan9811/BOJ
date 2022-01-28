from sys import stdin, stdout
input = stdin.readline
N = int(input())
L = []
for _ in range(N):
    L.append(int(input()))

L.sort()
for item in L:
    stdout.write(f"{item}\n")