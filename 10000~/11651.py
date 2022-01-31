from sys import stdin, stdout
N = int(stdin.readline())
L = [tuple(map(int, stdin.readline().split(' '))) for _ in range(N)]

L.sort(key = lambda x:(x[1], x[0]))
for item in L:
    stdout.write(f"{item[0]} {item[1]}\n")