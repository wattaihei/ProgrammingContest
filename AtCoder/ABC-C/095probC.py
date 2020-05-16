A, B, C, X, Y = map(int, input().split())


Set = min(X, Y)

if A+B >= 2*C:
    ans = Set * C * 2
    X -= Set
    Y -= Set
    big = max(X, Y)
    ans += min(A*X+B*Y, big*2*C)
else:
    ans = A*X + B*Y

print(ans)