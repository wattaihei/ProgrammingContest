import sys
input = sys.stdin.readline

import copy

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = copy.deepcopy(A)

for i in range(N):
    for j in range(N):
        for k in range(N):
            B[j][k] = min(B[j][k], B[j][i]+B[i][k])

INF = int(1E17)
ok = True
ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        if A[i][j] != B[i][j]:
            ok = False
        d = INF
        for k in range(N):
            if k == i or k == j:
                continue
            d = min(d, A[i][k] + A[k][j])
        if d > A[i][j]:
            ans += A[i][j]
                
if not ok:
    print(-1)
else:
    print(ans)