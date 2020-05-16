N, K = map(int, input().split()) 
X = list(map(int, input().split()))

Xs = [X[0]]
for i in range(N-1):
    Xs.append(Xs[-1]+X[i+1]-X[i])

ans = 2*(X[N-1] - X[0])
for i in range(N-K+1):
    zerodim = min(abs(X[i]), abs(X[i+K-1]))
    dis = Xs[K+i-1] - Xs[i]
    #print(X[i], X[i+K-1])
    #print(zerodim)
    #print(dis)
    ans = min(dis + zerodim, ans)

print(ans)