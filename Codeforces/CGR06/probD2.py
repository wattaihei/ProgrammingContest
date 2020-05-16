import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = [0]*N
for _ in range(M):
    a, b, d = map(int, input().split())
    A[a-1] += d
    A[b-1] -= d

Plus = []
Minus = []
for i in range(N):
    if A[i] > 0:
        Plus.append((i, A[i]))
    if A[i] < 0:
        Minus.append((i, -A[i]))

ans = []
ind = 0
for ip, pd in Plus:
    while pd > 0 and ind < len(Minus):
        im, md = Minus[ind]
        if pd >= md:
            ans.append((ip, im, md))
            ind += 1
            pd -= md
        else:
            ans.append((ip, im, pd))
            Minus[ind] = (im, md-pd)
            pd = 0

print(len(ans))
for p, m, d in ans:
    print(p+1,m+1,d)