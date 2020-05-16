N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

d = 0
u = 0
for i, a in enumerate(A):
    if i == 0:
        pre = a
        continue
    if a < pre:
        d += 1
        u = 0
        ans = i+1
    elif a > pre:
        if d < X:
            d = 0
        u += 1
    if u >= Y:
        break
    pre = a

if d == 0:
    ans = 1
print(ans)