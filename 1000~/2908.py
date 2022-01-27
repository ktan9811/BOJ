A, B = input().split(' ')
a = A[::-1]
b = B[::-1]

a = int(a)
b = int(b)

if a > b:
    print(a)
else:
    print(b)