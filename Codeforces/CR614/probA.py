import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, S, K = map(int, input().split())
    A = set(map(int, input().split()))
    Query.append((N, K, S, A))

for N, K, S, A in Query:
    c = 0
    while True:
        if (not S+c in A and S+c <= N) or (S-c > 0 and not S-c in A):
            break
        c += 1
    print(c)