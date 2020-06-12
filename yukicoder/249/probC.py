import sys
input = sys.stdin.readline

L, R = map(int, input().split())

P = set()
ans = 0
for n in range(L, R+1):
    if n in P: continue
    ans += 1
    t = 2*n
    while t <= R:
        P.add(t)
        t += n
print(ans-1)
