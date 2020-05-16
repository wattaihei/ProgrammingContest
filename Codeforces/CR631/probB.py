import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    leftOK = [True]*(N+1)
    already = set()
    MAX = 0
    for i, a in enumerate(A):
        if a in already:
            ok = False
        else:
            already.add(a)
            MAX = max(MAX, a)
            if len(already) == i+1 and MAX == i+1:
                ok = True
            else:
                ok = False
        leftOK[i+1] = ok
    
    rightOK = [True]*(N+1)
    already = set()
    MAX = 0
    for i in reversed(range(N)):
        a = A[i]
        if a in already:
            ok = False
        else:
            already.add(a)
            MAX = max(MAX, a)
            if len(already) == MAX and MAX == N-(i):
                ok = True
            else:
                ok = False
        rightOK[i] = ok

    ans = []
    for n in range(1, N):
        if leftOK[n] and rightOK[n]:
            ans.append(str(n) + " " + str(N-n))
    
    print(len(ans))
    print("\n".join(ans))