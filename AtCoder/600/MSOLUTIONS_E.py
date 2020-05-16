import sys
input = sys.stdin.readline
mod = 10**6+3
#mod = 13

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

T = [1]
for n in range(1, mod+1):
    T.append(T[-1]*n%mod)

for x, d, n in Query:
    start = x*pow(d, mod-2, mod)%mod
    if d == 0:
        ans = pow(x, n, mod)
    elif start == 0 or start + n-1 >= mod:
        ans = 0
    else:
        ans = pow(d, n, mod) * pow(T[start-1], mod-2, mod) * T[start+n-1] % mod
    print(ans)