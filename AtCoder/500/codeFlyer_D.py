H, W = map(int, input().split())
N, M = map(int, input().split())
state = [list(input()) for _ in range(N)]

S1 = [[0]*M for _ in range(N)]
for n in range(N):
    for m in range(M):
        if state[n][m] == '#' or S1[n][m-1] > 0:
            S1[n][m] += 1

for m in range(M):
    for n in range(1, N):
        if S1[n-1][m] > 0:
            S1[n][m] += 1

S2 = [[0]*M for _ in range(N)]
for n in range(N):
    for m in reversed(range(M)):
        if m == M-1:
            if state[n][m] == '#':
                S2[n][m] += 1
            continue
        if state[n][m] == '#' or S2[n][m+1] > 0:
            S2[n][m] += 1

for m in range(M):
    for n in range(1, N):
        if S2[n-1][m] > 0:
            S2[n][m] += 1

S3 = [[0]*M for _ in range(N)]
for n in range(N):
    for m in range(M):
        if state[n][m] == '#' or S3[n][m-1] > 0:
            S3[n][m] += 1

for m in range(M):
    for n in reversed(range(N-1)):
        if S3[n+1][m] > 0:
            S3[n][m] += 1

S4 = [[0]*M for _ in range(N)]
for n in range(N):
    for m in reversed(range(M)):
        if m == M-1:
            if state[n][m] == '#':
                S4[n][m] += 1
            continue
        if state[n][m] == '#' or S4[n][m+1] > 0:
            S4[n][m] += 1

for m in range(M):
    for n in reversed(range(N-1)):
        if S4[n+1][m] > 0:
            S4[n][m] += 1


B = [0]*4
for n in range(N):
    for m in range(M):
        if S1[n][m] == 0:
            B[0] += 1
        if S2[n][m] == 0:
            B[1] += 1
        if S3[n][m] == 0:
            B[2] += 1
        if S4[n][m] == 0:
            B[3] += 1

import pprint as pp
pp.pprint(S1)
pp.pprint(S2)
pp.pprint(S3)
pp.pprint(S4)

P1 = []
for n in range(N):
    black = False
    for m in range(M):
        if state[n][m] == '#':
            black = True
            break
    if black:
        P1.append(n)
P2 = []
for m in range(M):
    black = False
    for n in range(N):
        if state[n][m] == '#':
            black = True
            break
    if black:
        P2.append(m)

n1, n2 = N-1 - max(P1), min(P1)
m1, m2 = M-1 - max(P2), min(P2)

ans = H*W - sum(B) - (n1+n2)*(W-2*M) - (m1+m2)*(H-2*N)

print(ans)