S = input()
UCPC = "UCPC"
j = 0
for i in range(len(S)):
    if S[i] == UCPC[j]:
        j += 1
        if j == 4:
            print("I love UCPC")
            quit()

print("I hate UCPC")