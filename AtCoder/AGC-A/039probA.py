S = list(input())
K = int(input())

L = len(S)

a = 1
B = []
for i in range(L-1):
    if S[i] == S[i+1]:
        a += 1
    else:
        B.append(a)
        a = 1
B.append(a)

ans = 0
if S[0] != S[-1]:
    for b in B:
        ans += b // 2
    ans *= K
elif len(B) == 1:
    ans = L*K//2
else:
    for i in range(1, len(B)-1):
        ans += B[i]//2
    ans *= K
    ans += (B[0]+B[-1])//2 * (K-1)
    ans += B[0] // 2
    ans += B[-1] // 2

print(ans)