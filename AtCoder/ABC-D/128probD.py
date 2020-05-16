N, K = map(int, input().split())
V = list(map(int, input().split()))
ans = 0
for k in range(K+1):
    for n in range(k+1):
        if n >= N or k > N:
            break
        A = V[:n]
        A.extend(V[N-k+n:])
        A.sort()
        
        c = sum(A)
        for i in range(min(K-k, k)):
            if A[i] <= 0:
                c -= A[i]
        #print(k, n, c)
        ans = max(ans, c)
print(ans)