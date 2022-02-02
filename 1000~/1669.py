monkey, dog = map(int, input().split(' '))
height = dog - monkey
day = 0

while(True):
    if day % 2 == 1:
        if height <= (day//2 + 1) ** 2:
            break
    else :
        if height <= (day//2) * (day//2+1):
            break
    day += 1
print(day)