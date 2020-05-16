N = int(input())
S1 = list(input())
S2 = list(input())

mod = int(1E9+7)

if S1[0] == S2[0]:
    ans = 3
else:
    ans = 6
for i in range(N-1):
    if S1[i] != S1[i+1] and S1[i] == S2[i]:
        ans *= 2
    elif S1[i] == S2[i] and S1[i+1] == S2[i+1]:
        ans *= 3
    elif S1[i] != S2[i] and S1[i] != S1[i+1] and S2[i] != S2[i+1] and S1[i+1] != S2[i+1]:
        ans *= 3
    ans = ans % mod

print(ans)