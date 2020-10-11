import sys
input = sys.stdin.buffer.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    W = list(map(int, input().split()))
    Query.append((N, K, A, W))

for N, K, A, W in Query:
    A.sort()
    W.sort(reverse=True)
    count1 = W.count(1)
    W = W[:K-count1]
    ans = sum(A[N-K:]) + sum(A[N-count1:])
    ind = 0
    for w in W:
        ans += A[ind]
        ind += w-1
    print(ans)