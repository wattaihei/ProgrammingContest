import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append((N, K, A))

for N, K, A in Query:
    B = set(A)
    if len(B) > K:
        print(-1)
    else:
        n = 1
        while len(B) < K:
            if not n in B:
                B.add(n)
            n += 1
        
        T = list(B)
        ans = T * N
        print(len(ans))
        print(*ans)