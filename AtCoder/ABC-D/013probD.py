import sys
input = sys.stdin.readline

N, M, D = map(int, input().split())
A = list(map(int, input().split()))

E = [i for i in range(N)]

for a in A:
    tmp = E[a]
    E[a] = E[a-1]
    E[a-1] = tmp

F = [None]*N
for i, e in enumerate(E):
    F[e] = i

root = [-1]*N
seq = [-1]*N
dic = {}
for n in range(N):
    if root[n] != -1:
        continue
    p = n
    B = [n]
    root[n] = n
    seq[n] = 0
    for i in range(N+1):
        np = F[p]
        if np == n:
            break
        B.append(np)
        root[np] = n
        seq[np] = i+1
        p = np
    dic[n] = B

for n in range(N):
    r = root[n]
    l = len(dic[r])
    s = seq[n]
    d = D%l
    ans = dic[r][(s+d)%l]
    print(ans+1)