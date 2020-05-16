import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    S = set(A)
    C = set()
    for n in range(1, 2*N+1):
        if not n in S:
            C.add(n)
    
    ans = []
    for a in A:
        to = -1
        for n in range(a+1, 2*N+1):
            if n in C:
                to = n
                break
        if to == -1:
            ans = []
            break
        ans.append(a)
        ans.append(to)
        C.remove(to)
    
    if not ans:
        print(-1)
    else:
        print(*ans)