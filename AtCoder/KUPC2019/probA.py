N, X = map(int, input().split())
A = list(map(int, input().split()))

L = max(A)
ans = 0
for a in A:
    if a + X >= L:
        ans += 1
print(ans)