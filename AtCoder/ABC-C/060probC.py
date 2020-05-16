N, T = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
pre = 0
for a in A:
    ans += min(a-pre, T)
    pre = a

ans += T
print(ans)