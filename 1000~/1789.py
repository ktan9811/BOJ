a = int(input())

i = 0
sum = 0
while(True):
    i += 1
    sum += i
    if sum > a:
        break

print(i-1)