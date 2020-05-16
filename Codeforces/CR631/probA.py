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
    c = 0
    for v in range(1, N+K+3):
        if not v in B:
            if c == K:
                break
            c += 1
    print(v-1)
        