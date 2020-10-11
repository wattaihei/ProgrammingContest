A, B, X = map(int, input().split())
ans = 0
for d in range(1, 11):
    n = (X - B*d) // A
    ans = max(min(n, 10**d-1), ans)
ans = min(ans, 10**9)
print(ans)