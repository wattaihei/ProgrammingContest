import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, S = map(str, input().rstrip().split())
    Query.append((int(N), list(S)))

for N, S in Query:
    L = []
    for i, s in enumerate(S):
        if s == "<":
            L.append(i)
    L.append(N-1)
    Ls = set(L)
    Longans = [-1]*N
    Shortans = [-1]*N
    P = []
    k = []
    pre = -2
    for i, l in enumerate(L):
        Longans[l] = i+1
        if l == pre + 1:
            k.append(l)
        else:
            P.append(k)
            k = [l]
        pre = l
    P.append(k)
    
    count = 0
    for k in reversed(P):
        for n in k:
            count += 1
            Shortans[n] = count
    
    for i in reversed(range(N)):
        if not i in Ls:
            count += 1
            Longans[i] = count
            Shortans[i] = count
    
    print(*Shortans, sep=" ")
    print(*Longans, sep=" ")
