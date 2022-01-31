from sys import stdin, stdout
N = int(stdin.readline())
L = [list(stdin.readline().split(' ')) for i in range(N)]
L.sort(key = lambda x:int(x[0]))
for item in L:
    stdout.write(f"{item[0]} {item[1]}")
