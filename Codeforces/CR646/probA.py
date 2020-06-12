import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append((N, K, A))

for N, K, A in Query:
    dp = [0, 0]
    for a in A:
        dp[a%2] += 1
    ok = False
    for i in range(K):
        num_odd = 2*i+1
        num_even = K - num_odd
        if 0 <= num_even <= dp[0] and 0 <= num_odd <= dp[1]:
            ok = True
            break
    print("Yes" if ok else "No")