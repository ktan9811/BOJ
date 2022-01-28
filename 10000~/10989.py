import sys
input = sys.stdin.readline

N = int(input())
L = [0 for _ in range(10001)]

for i in range(N):
    L[int(input())] += 1

for i in range(len(L)):
    if L[i] != 0:
        for _ in range(L[i]):
            sys.stdout.write(f"{i}\n")

#if use print, memover in pypy3