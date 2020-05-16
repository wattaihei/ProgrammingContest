import sys
input = sys.stdin.readline

N, K, M = map(int, input().split())
A = list(map(int, input().split()))
p = M*N-sum(A)

if p <= K:
    print(max(p, 0))
else:
    print(-1)