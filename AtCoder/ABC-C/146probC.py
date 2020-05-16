A, B, X = map(int, input().split())

ans = 0
for l in reversed(range(1, 19)):
    r = X - B*l
    n = min(r//A, 10**l-1)
    ans = max(n, ans)
print(min(ans, 10**9))