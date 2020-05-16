S = list(input())
N = len(S)
mod = int(1E9+7)

P = S.count('?')

dpA = [0 for _ in range(N)]
dpAB = [0 for _ in range(N)]
dpC = [0 for _ in range(N)]

if S[0] == 'A' or S[0]=='?':
    dpA[0] = 1
ans = 0
for i, s in enumerate(S):
    if i == 0:
        continue
    if s == 'A':
        dpA[i] = dpA[i-1] + 1
        dpAB[i] = dpAB[i-1]
        dpC[i] = dpC[i-1]
    if s == 'B':
        dpA[i] = dpA[i-1]
        dpAB[i] = dpAB[i-1] + dpA[i-1]
        dpC[i] = dpC[i-1]
    if s == 'C':
        dpA[i] = dpA[i-1]
        dpAB[i] = dpAB[i-1]
        dpC[i] = dpC[i-1] + dpAB[i-1]
        ans += dpC[i]*3**P
    if s == '?':
        P -= 1
        dpA[i] = 3*dpA[i-1] + 1
        dpAB[i] = 3*dpAB[i-1] + dpA[i-1]
        dpC[i] = dpC[i-1] + dpAB[i-1]
        ans += dpC[i]*3**P
    dpA[i] %= mod
    dpAB[i] %= mod
    dpC[i] %= mod
    ans %= mod
print(dpA)
print(dpAB)
print(ans)
