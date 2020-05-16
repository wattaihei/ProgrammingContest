N = int(input())
X = list(map(int, input().split()))

X.sort()

a = 0
ans = 0
for i, x in enumerate(X):
    if i == 0:
        prex = x
        continue
    d = x - prex
    a += i*d
    ans += a
    prex = x
print(ans)