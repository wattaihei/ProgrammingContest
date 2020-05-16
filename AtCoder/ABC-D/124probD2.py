N, K = map(int, input().split())
S = input()

T = []
s0, s1 = 0, 0
for i in range(N):
    if S[i] == '1':
        if s0 != 0:
            T.append(s0)
        s1 += 1
        s0 = 0
    else:
        if s1 != 0:
            T.append(s1)
        s0 += 1
        s1 = 0
if s0 != 0:
    T.append(s0)
if s1 != 0:
    T.append(s1)


E = [0]
s = 0
for t in T:
    s += t
    E.append(s)
L = len(E)
ans = 0
if 2*K >= L:
    ans = N
elif L == 2:
    ans = N
else:
    if S[0] == '0':
        ans = E[2*K]
        for l in range(0, L-2*K-1):
            if l%2==1:
                ans = max(E[l+2*K+1] - E[l], ans)
            else:
                ans = max(E[l+2*K-1] - E[l], ans)
    else:
        ans = E[2*K]
        for l in range(0, L-2*K-1):
            if l%2==0:
                ans = max(E[l+2*K+1] - E[l], ans)
            else:
                ans = max(E[l+2*K-1] - E[l], ans)
print(ans)