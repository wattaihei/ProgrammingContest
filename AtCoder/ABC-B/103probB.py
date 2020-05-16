S = input()
T = input()

ans = 'No'
for i in range(len(S)):
    A = S[i:] + S[:i]
    if A == T:
        ans = 'Yes'

print(ans)