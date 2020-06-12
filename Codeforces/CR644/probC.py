import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    B = [[], []]
    for a in A:
        B[a%2].append(a)
    
    ok = False
    if len(B[0])%2 == 0:
        ok = True
    else:
        P = set(B[1])
        for b in B[0]:
            if b+1 in P or b-1 in P:
                ok = True
                break
    print("YES" if ok else "NO")