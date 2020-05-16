N = int(input())
X = [0 for _ in range(2*N)]
Y = [0 for _ in range(2*N)]
for _ in range(N):
    a, b = map(int, input().split())
    X[a] = 1
    Y[b] = 1
for _ in range(N):
    c, d = map(int, input().split())
    X[c] = -1
    Y[d] = -1

l = 0
a = 0
for x in X:
    l += x
    if x < 0 and l >= 0:
        a += 1
    l = max(l, 0)
r = 0
b = 0
for y in Y:
    r += y
    if y < 0 and r >= 0:
        b += 1
    r = max(r, 0)

print(min(a, b))