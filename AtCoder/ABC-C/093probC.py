X = list(map(int, input().split()))

X.sort()

A, B, C = X
k = 2*C - A - B
ans = k // 2
if k % 2 != 0:
    ans += 2

print(ans)