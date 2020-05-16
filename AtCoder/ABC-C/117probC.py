N, M = map(int, input().split()) # 横に2個
X = list(map(int, input().split()))

if N >= M:
    ans = 0
else:
    X = sorted(X)
    dif = []
    for i in range(M-1):
        dif.append(X[i+1] - X[i])
    dif.sort(reverse=True)
    ans = X[M-1] - X[0] - sum(dif[:N-1])

print(ans)