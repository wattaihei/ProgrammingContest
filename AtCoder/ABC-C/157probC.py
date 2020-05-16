import sys
input = sys.stdin.readline

N, M = map(int, input().split())
SC = [list(map(int, input().split())) for _ in range(M)]

ans = -1
for n in range(10**(N-1), 10**N):
    sn = str(n)
    ok = True
    for s, c in SC:
        if sn[s-1] != str(c):
            ok = False
    if ok:
        ans = n
        break

if N == 1:
    ok = True
    for s, c in SC:
        if c != 0:
            ok = False
    if ok:
        ans = 0
print(ans)