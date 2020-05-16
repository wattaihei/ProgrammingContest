M, K = map(int, input().split())

a = 1
ans = 1
S = 1
while S*K < M:
    a *= (2*K+1)
    S += a
    ans += 1
print(ans)