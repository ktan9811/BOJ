N = int(input())
numl = []
for i in range (N):
    numl.append(int(input()))

numl.sort(reverse=True)

sum = 0
plist = []
mlist = []
for num in (numl):
    if num > 1:
        plist.append(num)
    elif num == 1:
        sum += 1
    else:
        mlist.append(num)

plist.sort(reverse=True)
mlist.sort()

for i in range(0,len(plist),2):
    if i + 1 < len(plist):
        sum += plist[i]*plist[i+1]
    else: 
        sum += plist[i]

for i in range(0,len(mlist),2):
    if i + 1 < len(mlist):
        sum += mlist[i]*mlist[i+1]
    else: 
        sum += mlist[i]
print(sum)