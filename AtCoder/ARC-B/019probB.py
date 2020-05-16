S = input()
L = len(S)

unequal = []
for i in range(L):
    if S[i] != S[L-1-i]:
        unequal.append(i)

if not unequal:
    ans = 25*(L//2*2)
elif len(unequal) == 2:
    ans = 25*(L-2) + 24*2
else:
    ans = 25*L
print(ans)