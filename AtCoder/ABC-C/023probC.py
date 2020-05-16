from collections import Counter

R, C, K = map(int, input().split())
N = int(input())
RC = [list(map(int, input().split())) for _ in range(N)]

row = [0 for _ in range(R)]
col = [0 for _ in range(C)]
for r, c in RC:
    row[r-1] += 1
    col[c-1] += 1

Rc = [0 for _ in range(N+1)]
Cc = [0 for _ in range(N+1)]
for r in row:
    Rc[r] += 1
for c in col:
    Cc[c] += 1

ans = 0
for i in range(K+1):
    j = K - i
    ans += Rc[i]*Cc[j]

for r, c in RC:
    s = row[r-1] + col[c-1]
    if s == K:
        ans -= 1
    elif s == K + 1:
        ans += 1
print(ans)