import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    ok = False
    if sum(A)%2 == 1:
        ok = True
    else:
        even = False
        odd = False
        for a in A:
            if a%2 == 0:
                even = True
            else:
                odd = True
        if even and odd:
            ok = True
    print("YES" if ok else "NO")