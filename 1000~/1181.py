N = int(input())
WL = []
for _ in range(N):
    WL.append(input())
    
WL.sort(key = lambda x:(len(x),x))
temp = None
for item in WL:
    if item != temp:
        print(item)
        temp = item