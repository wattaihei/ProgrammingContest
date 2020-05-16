import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
A.sort()
ans = 10**14
for l in range(N):
    delta = (B[0] - A[l])%M
    ok = True
    for i in range(N-l):
        if (B[i]-A[i+l]-delta)%M != 0:
            ok = False
            break
    for i in range(N-l, N):
        if (B[i]-A[i+l-N]-delta)%M != 0:
            ok = False
            break
    if ok:
        ans = min(ans, delta)
print(ans)