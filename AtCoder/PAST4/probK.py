import sys
input = sys.stdin.buffer.readline

mod = 10**9
M = 21

K = int(input())
R = []
Ts = []
for _ in range(K):
    N = int(input())
    A = list(map(int, input().rstrip().split()))
    T = [0]*M
    r = 0
    for a in A:
        for m in range(a+1, M):
            r += T[m]
        T[a] += 1
    R.append(r)
    Ts.append(T)

Q = int(input())
Query = list(map(int, input().rstrip().split()))

ans = 0
Table = [0]*M
for i in Query:
    i -= 1
    ans += R[i]
    w = 0
    for n in reversed(range(M)):
        ans = (ans + w*Ts[i][n]) % mod
        w += Table[n]
        Table[n] += Ts[i][n]

print(ans)    