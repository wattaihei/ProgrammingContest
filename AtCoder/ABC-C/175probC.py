X, K, D = map(int, input().split())
if X < 0:
    X = -X
if X >= K*D:
    ans = X - K*D
else:
    n = X // D
    X %= D
    K -= n
    if K%2 == 0:
        ans = X
    else:
        ans = abs(X-D)
print(ans)