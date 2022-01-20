str = list(input().split('-'))
print(str)
def stoi(stdin):
    res = 0
    num = ''
    for char in stdin:
        if char == '+':
            res += int(num)
            num = ''
        else:
            num = num + char
    res += int(num)
    return res

sum = 0
sum += stoi(str[0])
for i in range(1,len(str)):
    sum -= stoi(str[i])
print(sum)