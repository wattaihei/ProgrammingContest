import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append((N, K, A))

for N, K, A in Query:
    P = []
    for i, a in enumerate(A):
        if i == 0 or i == N-1: continue
        if A[i-1] < a and a > A[i+1]:
            P.append(i)
    
    ans = 0
    score = 0
    p_ind = 0
    for i, p in enumerate(P):
        while p_ind < len(P) and P[p_ind] < p - 1 + K - 1:
            p_ind += 1
        if score < p_ind - i:
            score = p_ind - i
            ans = max(P[p_ind-1] - K+2, 0)
    print(score+1, ans+1)