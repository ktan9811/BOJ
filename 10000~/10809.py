S = input()
AL = [-1 for _ in range(26)]
for i in range(len(S)):
    if AL[ord(S[i]) - ord('a')] == -1:
        AL[ord(S[i]) - ord('a')] = i

for num in AL:
    print(num, end=' ')