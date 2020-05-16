import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    S = list(input().rstrip())
    Query.append((N, S))

for N, S in Query:
    P = []
    for i, s in enumerate(S):
        if s == "1":
            P.append(i)
    
    L = len(P)
    if L == 0:
        print(N)
    else:
        n1 = P[0]+1
        n2 = P[-1]+1
        ans = max([n2*2, (N-n1+1)*2, N+1])
        print(ans)