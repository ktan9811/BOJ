n = int(input())
numl = list(map(int, input().split(' ')))
numl.sort()
print(numl[0]*numl[len(numl) - 1])