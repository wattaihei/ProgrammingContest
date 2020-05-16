N, K = map(int, input().split()) # 横に2個
S = [int(i) for i in list(input())]

N0 = []
N1 = []
n0 = 0
n1 = 0
for s in S:
    if s == 0:
        if n1 > 0:
            N1.append(n1)
            n1 = 0
        n0 += 1
    if s == 1:
        if n0 > 0:
            N0.append(n0)
            n0 = 0
        n1 += 1
if n0 > 0:
    N0.append(n0)
if n1 > 0:
    N1.append(n1)

M0 = [0]
m0 = 0
for n0 in N0:
    m0 += n0
    M0.append(m0)

M1 = [0]
m1 = 0
for n1 in N1:
    m1 += n1
    M1.append(m1)
#print(M0)
#print(M1)

c = 0 if S[0] == 0 else 1

if len(N1) == 1 and len(N0) == 0:
    ans = N1[0]
elif len(N1) == 0 and len(N0) == 1:
    ans = N0[0]
else:
    ans = 0
    for i in range(N):
        if i + K >= len(M0):
            break
        if c == 0:
            if i == 0:
                l = M0[K] + M1[i+K]
            elif i == len(M1)-1:
                l = M0[i+K]-M0[i] + M1[i+K-1]-M1[i-1]
            else:
                l = M0[i+K]-M0[i] + M1[i+K]-M1[i-1]
        else:
            if i == len(M1)-2:
                l = M0[i+K]-M0[i] + M1[i+K]-M1[i]
            else:
                l = M0[i+K]-M0[i] + M1[i+K+1]-M1[i]
        #print(i, l)
        ans = max(ans, l)
print(ans)