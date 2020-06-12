import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    A.sort()
    ans = 0
    Ma = 0
    Mem = 0
    for a in A:
        Ma = max(Ma, a)
        Mem += 1
        if Ma <= Mem:
            ans += 1
            Ma = 0
            Mem = 0
    print(ans)